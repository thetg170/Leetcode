# Feature Specification — Local tests for NeetCode 150

**Feature Directory** `specs/006-neetcode-local-tests`  
**Created** 2026-11-10  
**Status** Implemented

## User Scenarios & Testing

### US1 — Test any NeetCode practice draft (P1)

In the Neovim workspace, press `Space l t` to save and test the current Python
draft. All 150 problems in the deck have a local suite. Curated cases include
ordinary and boundary behavior. Where the statement permits multiple valid
outputs, the tests validate the result rather than a single arbitrary ordering.

**Independent test** Start a new review attempt for a previously uncovered
problem. The stub does not pass, a wrong answer fails, and a correct draft
passes using the same keymap.

### US2 — Preserve the archive and established workflow (P1)

The 20 existing problem suites remain usable. Test the 130 added problem
suites against local references and through the existing target override.
Use the current timeout and result reporting. Preserve prior solutions,
starters, and drafts.

**Independent test** Run the full pytest suite and verify that all 150
per-problem suites execute through `lc test --path` in a disposable checkout.
Compare archived file and draft hashes and verify Git HEAD and index.

## Functional Requirements

- **FR-001** Add tests at the existing configured paths for exactly 130
  uncovered problems.
- **FR-002** Reuse the existing runner and target override. Validate stateful
  classes, node structures, in-place output and unordered or alternative
  answers according to the problem contract.
- **FR-003** Use independent fixtures with at least two checks per new
  problem, including a distinct branch, edge case or state transition.
- **FR-004** Preserve existing archive files, starter files, old tests and
  drafts. Do not commit or push.

## Success Criteria

- All 150 problems have a collected local suite.
- Known-good local targets pass through the CLI. The Neovim shortcut exercises
  the actual draft buffer and reports local failures.
- The implementation and verification do not overwrite archived solutions
  or draft files.
