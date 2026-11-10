# Implementation Plan — Local tests for NeetCode 150

## Summary

Add 130 pytest files at the current catalog paths. Reuse the existing
`KATA_TARGET` loader, fixtures and Neovim Test command. Partition authoring
into structured, scalar and legacy cases and validate in a disposable checkout.

## Technical Context

The NeetCode mapping contains 150 exact local selectors. Twenty have existing
curated suites. The 130 missing suites include 107 new Python references and
23 archived submissions. Tests can load a known-good path by default and
use the saved draft when the runner supplies the existing override.

## Constitution Check

Keep prior submissions and review drafts separate from tests. Add no runtime
dependencies. Treat results as local evidence independent of Anki, learning
status and LeetCode acceptance.

## Project Structure

- `<problem>/tests/test_solution.py` for the 130 missing suites.
- `tests/support/` for existing loaders, node types and narrowly shared helpers
  if needed.
- `README.md` and `practice/workspace-shortcuts.md` for verified coverage.

## Verification

Validate every new suite against a local reference, then execute all 150
configured files through the actual CLI with an explicit draft path. Exercise
the Neovim keymap with an unsaved correct answer, a wrong answer, and the
unimplemented starter. Check Git, archive, existing tests and draft integrity.
