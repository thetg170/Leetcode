# Data Model — Terminal LeetCode Workspace

## Problem

The stable key is the full directory name. Read the display title, numeric IDs, slug, language, difficulty, and archived file paths from the directory and its existing metadata when available. Numeric IDs and slugs can be ambiguous. Resolve an ambiguous selector only when the learner supplies a unique full directory name or another unique selector. Validate files under the selected problem or repository.

## Practice solution

Each problem has a separate `solution.py` or `solution.sql`. Create it only when needed and preserve an existing practice solution. The archived reference and any kata scratch file remain independent inputs. The runner uses the saved Python practice file.

## Statement and sample

- Statement summaries use `practice/statements/<directory>/<lang>.md` where language is `en` or `vi`. Prefer the requested language, then show a labeled fallback. If the archive statement is also missing, show the problem metadata and source link when available.
- A Python sample uses `practice/examples/<directory>.json`. It contains a method name, an ordered argument list, and an expected JSON value. Optional `unordered` allows comparison of a list regardless of order. The Two Sum sample is the initial fixture.

## Progress and notes

Progress lives in `practice/progress/<directory>.json`. The state is one of `not-started`, `in-progress`, `solved`, or `need-review`. A missing progress record starts as Not Started. The learner can explicitly mark any state, with the practice date recorded in the progress file. Tests and examples do not change this state. Notes append to the problem's Markdown notes file and preserve earlier entries.

## Workspace

A workspace belongs to one resolved checkout. It tracks the current problem, preferred language, and pane and editor identities. Runtime paths, generated statements, and socket endpoints are machine-specific. Store runtime state under ignored `practice/.lc/` or a private temporary directory. Git only shares the versioned practice data.
