# Tasks — Local tests for NeetCode 150

## Phase 1 — Setup

- [x] T001 Identify the 130 missing suites and record the behavior contracts under `specs/006-neetcode-local-tests/`.

## Phase 2 — US1: Add missing coverage

- [x] T002 [P] [US1] Add tests to 31 tree, linked-list and stateful problem directories.
- [x] T003 [P] [US1] Add tests to 81 other starter-based problem directories.
- [x] T004 [P] [US1] Add tests to 18 other legacy problem directories.

## Phase 3 — US2: Integration and verification

- [x] T005 [US2] Run the full suite, all 150 CLI targets and the real Neovim shortcut with pass and failure cases.
- [x] T006 [US2] Verify old files, drafts and Git are preserved, update workspace documentation, and record verification here.

## Dependencies and execution

T001 → T002, T003 and T004 in parallel on disjoint problem directories. Run
T005 after all suites pass against their defaults. Finish T006 after the
workspace path and preservation checks.

## Verification — 2026-11-10

- Added 130 suites at the configured paths. The full repository suite passed
  385 cases, including 352 new cases and the original 33. Ruff checks and
  formatting passed for all 130 files.
- All 150 configured suites ran successfully through the real `lc test --path`
  command against known-good disposable draft targets. Stateful and scalar
  wrong-answer checks verified that tests use the overridden draft.
- In isolated tmux, the real `Space l t` mapping on Invert Binary Tree reported
  Runtime Error for the starter, Failed for a wrong answer, and Passed after
  saving a modified correct answer. The result could be closed with `q`.
- Verified hashes for 1,740 pre-existing problem files, including archived
  implementations, starter files and original suites. Verification used
  disposable drafts. Git HEAD, index and `git diff --check` matched expectations.
