#include "InjectFuzzer.h"

#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendPluginRegistry.h"
#include "llvm/Support/raw_ostream.h"

using namespace clang;
using namespace ast_matchers;


// From https://www.py4u.net/discuss/94401

std::string get_source_text_raw(clang::SourceRange range, const clang::SourceManager& sm) {
    return clang::Lexer::getSourceText(clang::CharSourceRange::getCharRange(range), sm, clang::LangOptions());
}

std::string get_source_text(clang::SourceRange range, const clang::SourceManager& sm) {
    clang::LangOptions lo;

    // NOTE: sm.getSpellingLoc() used in case the range corresponds to a macro/preprocessed source.
    auto start_loc = sm.getSpellingLoc(range.getBegin());
    auto last_token_loc = sm.getSpellingLoc(range.getEnd());
    auto end_loc = clang::Lexer::getLocForEndOfToken(last_token_loc, 0, sm, lo);
    auto printable_range = clang::SourceRange{start_loc, end_loc};
    return get_source_text_raw(printable_range, sm);
}

//-----------------------------------------------------------------------------
// InjectFuzzer - implementation
//-----------------------------------------------------------------------------
void InjectFuzzerMatcher::run(const MatchFinder::MatchResult &Result) {
  // ASTContext is used to retrieve the source location
  ASTContext *Ctx = Result.Context;

  const char *FuzzBodyTemplate = R""""({

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("%1$s")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("%1$s", context);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          do_%1$s(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_%1$s(context);

      } else {
        do_%1$s(context);
      }

  })"""";


  const FunctionDecl *ComputeDecl =
      Result.Nodes.getNodeAs<clang::FunctionDecl>("computecall");

  Stmt *ComputeBody = ComputeDecl->getBody();

  assert(ComputeDecl && ComputeBody);

  const CXXRecordDecl* ParentClass;
  const auto Parents = Ctx->getParents(*ComputeDecl);

  for (auto ParentNode : Parents) {
    if (isa<CXXRecordDecl>(ParentNode.get<Decl>())){
      ParentClass = ParentNode.get<CXXRecordDecl>();
      break;
    }
  }

  StringRef OpName = ParentClass->getName();

  FullSourceLoc ComputeStartLoc = Ctx->getFullLoc(ComputeDecl->getBeginLoc());
  FullSourceLoc ComputeBodyStartLoc = Ctx->getFullLoc(ComputeBody->getBeginLoc());
  SourceRange ComputeSR = ComputeBody->getSourceRange();

  std::string ComputeText = get_source_text(ComputeSR, InjectFuzzerRewriter.getSourceMgr());

  char FilledBody[0x1000];
  char NewFname[0x100];
  memset(FilledBody, 0, 0x1000);
  memset(NewFname, 0, 0x100);
  sprintf(FilledBody, FuzzBodyTemplate, OpName.str().c_str());
  sprintf(NewFname, "void do_%s(OpKernelContext *context)", OpName.str().c_str());
  std::string FilledBodyStr(FilledBody);

  InjectFuzzerRewriter.InsertText(ComputeStartLoc, (Twine(NewFname) + ComputeText + "\n\n").str());
  /* InjectFuzzerRewriter.InsertText(ComputeEndLoc.getLocWithOffset(2), "Test 456\n", false); */
  /* InjectFuzzerRewriter.ReplaceText(ComputeStartLoc, ComputeSource); */
  InjectFuzzerRewriter.RemoveText(ComputeSR);
  InjectFuzzerRewriter.InsertText(ComputeBodyStartLoc, FilledBodyStr);

}

void InjectFuzzerMatcher::onEndOfTranslationUnit() {
  // Replace in place
  // InjectFuzzerRewriter.overwriteChangedFiles();

  // Output to stdout
  InjectFuzzerRewriter.getEditBuffer(InjectFuzzerRewriter.getSourceMgr().getMainFileID())
      .write(llvm::outs());

}

InjectFuzzerASTConsumer::InjectFuzzerASTConsumer(Rewriter &R) : InjectFuzzerHandler(R) {
  DeclarationMatcher CallSiteMatcher =
      functionDecl(hasName("Compute"))
    .bind("computecall");


  // InjectFuzzer is the callback that will run when the ASTMatcher finds the pattern
  // above.
  Finder.addMatcher(CallSiteMatcher, &InjectFuzzerHandler);
}

//-----------------------------------------------------------------------------
// FrotendAction
//-----------------------------------------------------------------------------
class InjectFuzzerPluginAction : public PluginASTAction {
public:
  // Our plugin can alter behavior based on the command line options
  bool ParseArgs(const CompilerInstance &,
                 const std::vector<std::string> &) override {
    return true;
  }

  // Returns our ASTConsumer per translation unit.
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
