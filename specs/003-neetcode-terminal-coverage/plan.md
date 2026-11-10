# Implementation Plan — Complete NeetCode 150 terminal coverage

## Summary

Add the 107 missing entries in the repository's numbered directory structure.
Use existing `meta.toml` and statement override conventions. Expand the shared
Python node types for problems that use trees, graph neighbors or random pointers.
Update the front of the 107 existing Anki notes after testing the terminal path.

## Technical Context

- NeetCode's published JSON and the current Anki deck identify the same 150
  problems used for the earlier import. The current catalog has 43 corresponding
  entries and 20 curated test suites.
- Map by the LeetCode problem slug. Some existing repo prefixes differ from
  the published problem number, so commands use the exact local directory name.
- `lc review` already loads a problem's configured reference and builds an
  unimplemented draft from its signatures.
- Existing EN/VI rendering reads the problem's English Markdown and
  `practice/statements/<directory>/vi.md` for Vietnamese.
- Use the existing AnkiConnect version 6 service on localhost.

## Constitution Check

Keep prior archive files and scratch work in place. Use original summaries and
offline fixtures. Store review attempts in the existing ignored directory and
preserve Anki scheduling. The change adds no dependencies or Git operations
against a remote.

## Project Structure

- `<directory>/README.md`, `meta.toml`, and `starter.py` for each new problem.
- `practice/statements/<directory>/vi.md` for translated original summaries.
- `tests/support/nodes.py` and `tools/kata.py` for types shared by Python drafts.
- `README.md` for coverage and launch instructions.

## Verification

Compare the deck against the canonical slug mapping. Check all 150 selectors and
invoke all commands in a temporary copy with an isolated tmux server. Verify
archive hashes, legacy pytest, and stable Anki note/card state.
