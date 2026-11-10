# Tasks — Terminal LeetCode Workspace

**Input** [Specification](spec.md), [plan](plan.md), [research](research.md), [data model](data-model.md), [CLI contract](contracts/cli.md), and [quickstart](quickstart.md).

## Phase 1 — Setup

- [x] T001 Audit both repositories and record the baseline in `specs/001-terminal-leetcode-workspace/plan.md`.
- [x] T002 Set up Spec Kit in `.specify/` and `.agents/skills/`, then create the feature documents in `specs/001-terminal-leetcode-workspace/`.

## Phase 2 — Foundation

- [x] T003 Wire the portable `bin/lc` launcher and CLI dispatch in `tools/lc.py`. Keep machine state under ignored `practice/.lc/` or a private temporary directory as recorded in `.gitignore`.

## Phase 3 — US1: Pick and edit a problem (P1)

**Goal** Read the problem and edit a practice solution in one tmux workspace.

**Independent test** From outside the checkout, use the picker and explicit selectors. Exercise ambiguity and the numbered fallback. Switch to another problem, return to the modified buffer, and reattach after detach.

- [x] T004 [US1] Discover archived problems and implement `list`, `search`, and problem selection in `tools/lc.py`. Handle duplicate IDs or slugs, and offer a numbered picker when fzf is unavailable.
- [x] T005 [US1] Implement `pick`, `open`, `next`, and `resume` in `tools/lc.py`, `tools/lc_workspace.py`, and `tools/lc_nvim.lua`. Create a separate `<problem>/solution.py` or `<problem>/solution.sql` only when needed. Preserve the editor and modified buffers while switching.

## Phase 4 — US2: Read in English or Vietnamese (P1)

**Goal** Read either available language independently of the editor.

**Independent test** Toggle both Two Sum summaries with a modified editor buffer. For other problems, verify labeled fallback and a metadata view when the source statement is absent.

- [x] T006 [P] [US2] Validate both authored Two Sum summaries in `practice/statements/0001-two-sum/en.md` and `practice/statements/0001-two-sum/vi.md`.
- [x] T007 [US2] Implement `lang en`, `lang vi`, and `lang toggle` with local rendering and a labeled fallback in `tools/lc.py` and `tools/lc_nvim.lua`.

## Phase 5 — US3: Run examples and tests (P1)

**Goal** Check the saved Python practice solution and distinguish local outcomes.

**Independent test** With a disposable solution, verify a passing run, wrong answer, runtime error, timeout, missing cases, and unsupported SQL execution. Trigger Test from a modified editor buffer and verify the saved version runs.

- [x] T008 [P] [US3] Validate the Two Sum fixture in `practice/examples/0001-two-sum.json`. It contains a method name, an ordered argument list, and an expected JSON value. Optional `unordered` allows comparison of a list regardless of order.
- [x] T009 [US3] Implement sample execution and curated pytest execution in `tools/lc_runner.py` and `tools/lc_pytest.py`. Report input, expected, and actual for the example. Provide clear errors for unavailable cases and unsupported languages.
- [x] T010 [US3] Wire Run and Test shortcuts in `tools/lc_nvim.lua` to save the active practice file and display the resulting output.

## Phase 6 — US4: Track and resume on another Mac (P2)

**Goal** Share reviewable practice data and sync with a deliberate Git workflow.

**Independent test** Mark and read each status, add a note, then bootstrap a second checkout with a space in its path. Exercise a clean fast-forward, dirty checkout, conflicted checkout, divergent history, and open editor with disposable fixtures.

- [x] T011 [US4] Implement `status`, `mark`, and `note` in `tools/lc.py`. Store progress under `practice/progress/<directory>.json`. The state is one of `not-started`, `in-progress`, `solved`, or `need-review`. Append notes to the problem's Markdown notes file.
- [x] T012 [US4] Complete setup and dependency diagnostics in `tools/bootstrap-lc.sh` and `tools/lc.py`. Test setup outside the original checkout path.
- [x] T013 [US4] Implement clean-checkout, closed-editor, fast-forward-only sync in `tools/lc.py`.

## Phase 7 — Verification and documentation

- [x] T014 Add Vietnamese setup, controls, and manual Git instructions to `README.md`, and align the examples in `specs/001-terminal-leetcode-workspace/quickstart.md`.
- [x] T015 Run the original pytest suite and verify the workflow in an isolated tmux server and a disposable checkout. Record the observed results in `specs/001-terminal-leetcode-workspace/tasks.md`.

## Dependencies and execution

Phase 1 → Phase 2 → US1. US2 and US3 each build on US1 and can be validated independently. US4 uses the shared CLI and checks that the US1 workspace is closed before pulling. Finish with Phase 7.

The US2 summaries and US3 JSON fixture touch separate files and can be checked in parallel with each other and with catalog implementation. Integrate code that touches the shared CLI and Lua files sequentially.

Deliver the picker and stable editor first, add the language viewer and local verification next, then add progress and sync. The approved MVP includes all four stories.

## Verification record — 2026-11-10

- **FR-001** Listed all 495 directories. Verified unique selector, duplicate ID error, fzf selection, and numbered fallback in an attached terminal.
- **FR-002** Opened both panes in isolated tmux and verified the 44-column stacked layout. Opened the popup, detached, resumed, and switched problems without replacing the editor. Modified content survived switching out and back. Verified that the archive's 1,311 pre-existing files and dotfiles changes retained their hashes.
- **FR-003** Captured EN, VI, the labeled EN fallback and a missing-statement view. Language changes preserved the unsaved editor buffer.
- **FR-004** Existing pytest suite passed 33/33. Verified Run and Test success, wrong answer, runtime error, and timeout with code 124, plus absent cases and SQL diagnostics. The real Neovim Test mapping saved the buffer and displayed the passing result. Verified switching to a different problem with a result window still open.
- **FR-005** Exercised all four progress states. Read the final Need Review status and appended note from a fresh local clone. A passing test left progress independent.
- **FR-006** Bootstrapped a fresh clone in a directory containing spaces. Exercised a local fast-forward and refusals for a dirty tree, an open editor, merge conflict and divergent histories. Used a disposable local remote for these cases.
- Ruff formatting and lint, basedpyright, shell syntax, and `git diff --check` passed.
