# Feature Specification — Practice from an Anki card

**Feature Directory** `specs/002-anki-review-drafts`  
**Created** 2026-11-10  
**Status** Implemented

## User Scenarios & Testing

### US1 — Solve today's card from scratch (P1)

An Anki card shows a problem and a terminal command. Run `lc review 0001-two-sum`
from anywhere to open the named problem in the existing workspace, with a fresh
Python draft. Run the sample or curated tests on the draft, then grade the card
in Anki.

**Independent test** Keep a saved solution for Two Sum. Open a review, write and
test a different solution, then verify the saved file's bytes and learning
status are unchanged. Run the same review command again and confirm the draft
starts fresh while the previous attempt remains available locally.

### US2 — Switch between reviewing and normal practice (P2)

Change statement language, switch back to the normal solution, or detach and
resume. Preserve edited buffers and route each test to the right file.

**Independent test** Verify editor Run/Test and argument-free CLI Run/Test on
the active draft. An explicit problem selector tests the regular solution.
Resume a saved draft after restarting the editor. An older workspace session
without a recorded draft continues to open and test the regular solution.

## Functional Requirements

- **FR-001** `lc review <problem>` accepts the same selectors as `lc open`.
  Python drafts start from the archived method signature when available.
- **FR-002** A new invocation creates a separate ignored draft for each attempt.
  No existing draft, scratch file or solution is overwritten.
- **FR-003** The statement identifies review mode. Language toggling and resume
  keep the active attempt. Editor and CLI checks use the existing Python runner.
- **FR-004** Anki owns scheduling and grading. The workflow uses a plain command
  in the card and works offline with the existing project dependencies.
- **FR-005** The CLI gives clear errors for unsupported languages and missing
  local cases, while the normal workspace continues to work.

## Success Criteria

- A Two Sum card's command opens a fresh draft and both Run and Test use it.
- Two attempts have distinct ignored paths. Switching and resuming preserves
  edited content and the archived and tracked solutions.
- Documentation shows how to add the command to an Anki card and what is shared
  between machines.
