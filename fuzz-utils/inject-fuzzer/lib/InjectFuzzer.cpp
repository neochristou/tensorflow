#include "InjectFuzzer.h"

#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendPluginRegistry.h"
#include "llvm/Support/raw_ostream.h"

using namespace clang;
using namespace ast_matchers;


// From https://www.py4u.net/discuss/94401

std::string get_source_text_raw(SourceRange range, const SourceManager& sm)
{
  return Lexer::getSourceText(CharSourceRange::getCharRange(range), sm, LangOptions()).str();
}

std::string get_source_text(SourceRange range, const SourceManager& sm)
{
  LangOptions lo;

  // NOTE: sm.getSpellingLoc() used in case the range corresponds to a macro/preprocessed source.
  auto start_loc = sm.getSpellingLoc(range.getBegin());
  auto last_token_loc = sm.getSpellingLoc(range.getEnd());
  auto end_loc = Lexer::getLocForEndOfToken(last_token_loc, 0, sm, lo);
  auto printable_range = SourceRange{start_loc, end_loc};
  return get_source_text_raw(printable_range, sm);
}

//-----------------------------------------------------------------------------
// InjectFuzzer - implementation
//-----------------------------------------------------------------------------
void ComputeDeclMatcher::run(const MatchFinder::MatchResult &Result) {

  char FilledBody[0x1000];
  char NewFname[0x100];

  const char *FuzzBodyTemplate = R""""({

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("%1$s")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("%1$s", %2$s);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_%1$s(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_%1$s(%2$s);

      } else {
        do_%1$s(%2$s);
      }

  })"""";

  llvm::outs() << "Match\n";

  // ASTContext is used to retrieve the source location
  ASTContext *Ctx = Result.Context;

  const FunctionDecl *ComputeDecl =
    Result.Nodes.getNodeAs<clang::FunctionDecl>("computedecl");

  if (!ComputeDecl) {
    return;
  }

  const CXXRecordDecl* ParentClass;
  const auto Parents = Ctx->getParents(*ComputeDecl);

  for (auto ParentNode : Parents) {
    if (isa<CXXRecordDecl>(ParentNode.get<Decl>())){
      ParentClass = ParentNode.get<CXXRecordDecl>();
      break;
    }
  }

  StringRef OpName = ParentClass->getName();

  if (ComputeDecl->getNumParams() > 1) {
    llvm::outs() << "Skipping " << OpName << " (>1 params)\n";
    return;
  }

  if (ComputeDecl->getStorageClass() == SC_Static) {
    llvm::outs() << "Skipping " << OpName << " (static)\n";
    return;
  }

  // Skip gradops for now
  /* if (OpName.endswith("GradOp")) { */
  /*   llvm::outs() << "Skipping " << OpName << " (GradOp)\n"; */
  /*   return; */
  /* } */

  // Skip SummaryOps
  if (OpName.contains("SummaryOp")) {
    llvm::outs() << "Skipping " << OpName << " (SummaryOp)\n";
    return;
  }

  /* if (OpName.startswith("BoostedTreesCreate")) { */
  /*   llvm::outs() << "Skipping " << OpName << " (BoostedTreesCreate)\n"; */
  /*   return; */
  /* } */

  Stmt *ComputeBody = ComputeDecl->getBody();

  if (!ComputeBody) {
    llvm::outs() << "Skipping " << OpName << " (no body)\n";
    return;
  }

  StringRef CtxParamName = ComputeDecl->parameters()[0]->getName();

  if (CtxParamName.empty()) {
    llvm::outs() << "Skipping " << OpName << " (no param name)\n";
    return;
  }

  FullSourceLoc ComputeStartLoc = Ctx->getFullLoc(ComputeDecl->getBeginLoc());
  FullSourceLoc ComputeBodyStartLoc = Ctx->getFullLoc(ComputeBody->getBeginLoc());
  SourceRange ComputeSR = ComputeBody->getSourceRange();

  std::string ComputeText = get_source_text(ComputeSR, InjectFuzzerRewriter.getSourceMgr());

  if (ComputeText.find(std::string("ResourceMgr")) != std::string::npos) {
    llvm::outs() << "Skipping " << OpName << " (ResourceMgr)\n";
    return;
  }

  /* if (ComputeText.find(std::string("PhiloxRandom")) != std::string::npos) { */
  /*   llvm::outs() << "Skipping " << OpName << " (PhiloxRandom)\n"; */
  /*   return; */
  /* } */

  if (ComputeText.find(std::string("mutex")) != std::string::npos ||
      ComputeText.find(std::string("Mutex")) != std::string::npos
      ) {
    llvm::outs() << "Skipping " << OpName << " (mutex)\n";
    return;
  }

  memset(FilledBody, 0, 0x1000);
  memset(NewFname, 0, 0x100);
  sprintf(FilledBody, FuzzBodyTemplate, OpName.str().c_str(), CtxParamName.str().c_str());
  sprintf(NewFname, "void do_%s(OpKernelContext *%s)", OpName.str().c_str(), CtxParamName.str().c_str());
  std::string FilledBodyStr(FilledBody);

  InjectFuzzerRewriter.InsertText(ComputeStartLoc, (Twine(NewFname) + ComputeText + "\n\n").str());
  InjectFuzzerRewriter.RemoveText(ComputeSR);
  InjectFuzzerRewriter.InsertText(ComputeBodyStartLoc, FilledBodyStr);

  llvm::outs() << "Successfully modified " << OpName << "\n";
  return;

}

void ComputeDeclMatcher::onEndOfTranslationUnit() {
  // Replace in place
  InjectFuzzerRewriter.overwriteChangedFiles();

  // Output to stdout
  /* InjectFuzzerRewriter.getEditBuffer(InjectFuzzerRewriter.getSourceMgr().getMainFileID()) */
  /*     .write(llvm::outs()); */
}

InjectFuzzerASTConsumer::InjectFuzzerASTConsumer(Rewriter &R) : ComputeDeclHandler(R) {

  DeclarationMatcher ComputeDeclMatcher =
    functionDecl(hasName("Compute"))
    .bind("computedecl");

  // InjectFuzzer is the callback that will run when the ASTMatcher finds the pattern
  // above.
  Finder.addMatcher(ComputeDeclMatcher, &ComputeDeclHandler);
}

//-----------------------------------------------------------------------------
// FrotendAction
//-----------------------------------------------------------------------------
class InjectFuzzerPluginAction : public PluginASTAction {
  public:
    bool ParseArgs(const CompilerInstance &,
                   const std::vector<std::string> &) override {
      return true;
    }

    std::unique_ptr<ASTConsumer> CreateASTConsumer(CompilerInstance &CI,
                                                   StringRef file) override {
      RewriterForInjectFuzzer.setSourceMgr(CI.getSourceManager(), CI.getLangOpts());
      return std::make_unique<InjectFuzzerASTConsumer>(RewriterForInjectFuzzer);
    }

  private:
    Rewriter RewriterForInjectFuzzer;
};

//-----------------------------------------------------------------------------
// Registration
//-----------------------------------------------------------------------------
static FrontendPluginRegistry::Add<InjectFuzzerPluginAction>
X(/*Name=*/"InjectFuzzer",
  /*Desc=*/"Inject fuzzing code in tensorflow kernels");
