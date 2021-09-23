#ifndef INJECT_FUZZER_H
#define INJECT_FUZZER_H

#include "clang/AST/ASTConsumer.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/Rewrite/Core/Rewriter.h"

//-----------------------------------------------------------------------------
// ASTMatcher callback
//-----------------------------------------------------------------------------
class InjectFuzzerMatcher : public clang::ast_matchers::MatchFinder::MatchCallback {
public:
  InjectFuzzerMatcher(clang::Rewriter &InjectFuzzerRewriter) : InjectFuzzerRewriter(InjectFuzzerRewriter) {}
  // Callback that's executed whenever the Matcher in InjectFuzzerASTConsumer
  // matches.
  void run(const clang::ast_matchers::MatchFinder::MatchResult &) override;
  // Callback that's executed at the end of the translation unit
  void onEndOfTranslationUnit() override;

private:
  clang::Rewriter InjectFuzzerRewriter;
  llvm::SmallSet<clang::FullSourceLoc, 8> EditedLocations;
};

//-----------------------------------------------------------------------------
// ASTConsumer
//-----------------------------------------------------------------------------
class InjectFuzzerASTConsumer : public clang::ASTConsumer {
public:
  InjectFuzzerASTConsumer(clang::Rewriter &R);
  void HandleTranslationUnit(clang::ASTContext &Ctx) override {
    Finder.matchAST(Ctx);
  }

private:
  clang::ast_matchers::MatchFinder Finder;
  InjectFuzzerMatcher InjectFuzzerHandler;
};

#endif
