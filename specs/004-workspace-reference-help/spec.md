# Feature Specification — Workspace reference and keyboard help

**Feature Directory** `specs/004-workspace-reference-help`  
**Created** 2026-11-10  
**Status** Implemented

## User Scenarios & Testing

### US1 — Inspect a reference while working (P1)

From a regular solution or an Anki draft, press `Space l s` in normal mode.
If the problem has a local archived solution, display it in a scrollable,
read-only preview. Press `q` or `Esc` to return to the same draft and cursor.
When the problem has only a starter, report that a local reference is
unavailable and point to the Anki answer or the source link.

**Independent test** Insert an unsaved line in a Two Sum review draft, open
and close its reference, and verify the buffer identity, content, cursor, and
modified state. Open a starter-only problem and verify the warning.

### US2 — Look up the workspace keys (P1)

Press `Space l h` to open a keyboard reference in the editor. It covers saving,
closing results, detaching and resuming, exiting, testing, and selecting or
viewing a problem. The README points to the same table.

**Independent test** Open the help with an unsaved draft, read the save, test
and exit instructions, then close it and continue editing.

## Functional Requirements

- **FR-001** Resolve the reference from the actual workspace buffer and its
  problem metadata. The reference action is local and read-only.
- **FR-002** Open help and references separately from the draft. Closing them
  preserves draft identity, modified content and cursor. Switching from the
  shell while a preview is open returns to the regular editing window.
- **FR-003** Explain missing or starter-only references in the editor.
- **FR-004** Maintain one shared Markdown table. Keep current Run/Test and
  workspace controls and dotfiles in place.
- **FR-005** Make the shortcuts loadable in an attached workspace without
  replacing its buffers. Do not commit or push.

## Success Criteria

- Both shortcuts work from the right-hand workspace editor.
- Reference lookup respects a draft from an earlier problem still open in
  Neovim. Viewing a reference never saves the draft or edits the archive.
- The existing pytest suite and the current workspace actions remain usable.
