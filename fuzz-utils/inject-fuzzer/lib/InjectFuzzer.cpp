#include "InjectFuzzer.h"

#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/FrontendPluginRegistry.h"
#include "llvm/Support/raw_ostream.h"

const std::string KERNEL_DIR = "/media/ivysyn/tensorflow/tensorflow/core/kernels/";

using namespace clang;
using namespace ast_matchers;

std::string get_source_filename(const SourceManager& SrcMgr, SourceLocation SrcLoc)
{
  const FileEntry* Entry = SrcMgr.getFileEntryForID(SrcMgr.getFileID(SrcLoc));
  return Entry->getName().str();
}

// From https://www.py4u.net/discuss/94401
std::string get_source_text_raw(SourceRange range, const SourceManager& SrcMgr)
{
  return Lexer::getSourceText(CharSourceRange::getCharRange(range), SrcMgr, LangOptions()).str();
}

std::string get_source_text(SourceRange range, const SourceManager& SrcMgr)
{
  LangOptions lo;

  // NOTE: SrcMgr.getSpellingLoc() used in case the range corresponds to a macro/preprocessed source.
  auto start_loc = SrcMgr.getSpellingLoc(range.getBegin());
  auto last_token_loc = SrcMgr.getSpellingLoc(range.getEnd());
  auto end_loc = Lexer::getLocForEndOfToken(last_token_loc, 0, SrcMgr, lo);
  auto printable_range = SourceRange{start_loc, end_loc};
  return get_source_text_raw(printable_range, SrcMgr);
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

  ASTContext *Ctx = Result.Context;
  const SourceManager &SrcMgr = InjectFuzzerRewriter.getSourceMgr();

  const FunctionDecl *ComputeDecl =
    Result.Nodes.getNodeAs<FunctionDecl>("computedecl");

  std::string SourceFile = get_source_filename(SrcMgr, ComputeDecl->getLocation());

  if (SourceFile != InputFilename) {
    /* llvm::outs() << SourceFile << " " << InputFilename << "\n"; */
    return;
  }

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

  if (OpName == "OpKernel" || OpName == "AsyncOpKernel") {
    return;
  }

  llvm::outs() << "Found Compute() call in " << OpName << "\n";

  if (ComputeDecl->getNumParams() > 1) {
    llvm::outs() << "Skipping " << OpName << " (>1 params)\n";
    return;
  }

  if (ComputeDecl->getNumParams() == 0) {
    llvm::outs() << "Skipping " << OpName << " (no params)\n";
    return;
  }

  if (ComputeDecl->getStorageClass() == SC_Static) {
    llvm::outs() << "Skipping " << OpName << " (static)\n";
    return;
  }

  if (OpName.contains("SummaryOp")) {
    llvm::outs() << "Skipping " << OpName << " (SummaryOp)\n";
    return;
  }

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

  std::string ComputeText = get_source_text(ComputeSR, SrcMgr);

  if (ComputeText.find(std::string("ResourceMgr")) != std::string::npos) {
    llvm::outs() << "Skipping " << OpName << " (ResourceMgr)\n";
    return;
  }

  if (ComputeText.find(std::string("mutex")) != std::string::npos ||
      ComputeText.find(std::string("Mutex")) != std::string::npos
      ) {
    llvm::outs() << "Skipping " << OpName << " (mutex)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "batch_kernels.cc") {
    llvm::outs() << "Skipping " << OpName << " (batch kernel)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "isotonic_regression_op.cc") {
    llvm::outs() << "Skipping " << OpName << " (isotonic regression)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "fact_op.cc") {
    llvm::outs() << "Skipping " << OpName << " (fact op)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "random_op.cc") {
    llvm::outs() << "Skipping " << OpName << " (random op)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "resource_variable_ops.cc") {
    llvm::outs() << "Skipping " << OpName << " (resource variable)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "list_kernels.cc") {
    llvm::outs() << "Skipping " << OpName << " (list kernel)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "list_kernels.h") {
    llvm::outs() << "Skipping " << OpName << " (list kernel)\n";
    return;
  }

  if (SourceFile == KERNEL_DIR + "tensor_array_ops.cc") {
    llvm::outs() << "Skipping " << OpName << " (tensor array)\n";
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

InjectFuzzerASTConsumer::InjectFuzzerASTConsumer(Rewriter &R, std::string &InpF) : ComputeDeclHandler(R, InpF) {

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
                   const std::vector<std::string> &Args) override {
      return true;
    }

    std::unique_ptr<ASTConsumer> CreateASTConsumer(CompilerInstance &CI,
                                                   StringRef file) override {
      std::string InpF = file.str();
      RewriterForInjectFuzzer.setSourceMgr(CI.getSourceManager(), CI.getLangOpts());
      return std::make_unique<InjectFuzzerASTConsumer>(RewriterForInjectFuzzer, InpF);
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
