# Feature Specification — Terminal LeetCode Workspace

**Feature Directory** `specs/001-terminal-leetcode-workspace`  
**Created** 2026-11-10  
**Status** Implemented

## User Scenarios & Testing

### US1 — Pick a problem and edit alongside its statement (P1)
From any directory, run `lc` and select a problem. See the statement and a real Neovim editor together. Select a different problem in the same session, then return to the previous unsaved buffer. Detach and reattach to the same editor. A narrow terminal can zoom the current pane and switch between panes.

### US2 — Read in English or Vietnamese (P1)
Open Two Sum and toggle between locally available EN and VI explanations. The editor and unsaved changes survive the toggle. For a missing translation, the statement identifies the displayed language and fallback. A missing statement displays problem metadata and a source link if available.

### US3 — Run examples and tests (P1)
Run a local example showing input, expected and actual output. Run the existing curated Python tests against the user's saved solution. Check passing, wrong answer, runtime error, timeout and unavailable test cases. The Neovim shortcut saves the current solution before testing. No local result changes acceptance or learning status.

### US4 — Resume on a second Mac (P2)
Record and list Not Started, In Progress, Solved and Need Review. Keep solutions, notes and progress in reviewable files. Bootstrap from a checkout at a different path. Refuse pull on a dirty or conflicted tree and refuse a non-fast-forward update.

## Requirements

- **FR-001** Discover archived problems in place. Support numeric IDs, slugs and full directory names, with disambiguation for duplicate IDs and a numbered picker if fuzzy search is unavailable.
- **FR-002** Preserve archived files and current dotfiles. Create separate tracked solutions and reuse the same editor session during problem switches.
- **FR-003** Prefer local statement files and show a clear fallback. Include one original bilingual example and support user-authored additions. Use no statement downloads or translation API.
- **FR-004** Reuse the existing test contract for curated Python problems. Provide an extensible example format for Python functions with JSON arguments. Surface unsupported languages and absent tests explicitly.
- **FR-005** Keep four learning statuses independent of local test outcomes. Support existing notes and review metadata without migrating them.
- **FR-006** Provide bootstrap, dependency diagnostics and manual sync instructions. Keep runtime state separate from versioned files.

## Success Criteria

- From outside the checkout, a picker or explicit command can open Two Sum with two panes, toggle language and select another problem without restarting the editor.
- Local verification covers pass, fail, runtime error, timeout, missing cases and safe Git sync using disposable local checkouts.
- A clean clone can bootstrap with its own directory path and read committed solutions and progress without machine-local files.
