# Practice metadata

Each active Python problem owns a `meta.toml`. Accepted LeetHub files remain the
reference implementation; generated `kata.py` and `buggy.py` files are scratch
buffers and are ignored by Git.

## `meta.toml` schema

```toml
schema_version = 1

[problem]
repo_id = 1                 # numeric prefix used by this repository
frontend_id = 1             # LeetCode display id
directory = "0001-two-sum"
slug = "two-sum"
title = "Two Sum"
language = "python"
difficulty = "easy"
source_url = "https://leetcode.com/problems/two-sum"
active = true

[files]
statement = "README.md"
reference = "0001-two-sum.py"
tests = "tests/test_solution.py"

[classification]
tags = ["Array", "Hash Table"]
patterns = ["hash-map"]
pattern_verified = false    # true after manually reviewing the imported tags

[review]
state = "learning"
queue = "core"             # core is scheduled; backlog is available in the picker
seed_order = 1
level = -1                  # index in the interval ladder before the first grade
due = "2026-09-16"
last_reviewed = ""
attempts = 0
lapses = 0
last_grade = ""
```

## Review states

- `new`: imported but not yet in the active core queue.
- `learning`: in the active queue and moving through the interval ladder.
- `review`: has reached at least the 14-day interval.
- `suspended`: intentionally excluded from scheduling.
- `incomplete`: statement exists but the reference solution is missing.

## Grades

The interval ladder is `1, 3, 7, 14, 30, 60` days.

- `again`: reset to level 0 and review tomorrow.
- `hard`: keep the level and repeat its interval.
- `good`: advance one level.
- `easy`: advance two levels.

`practice/sessions.jsonl` is append-only. Each line records the session timer,
test runs, failed runs, grade, motion focus, and a short reflection. Runtime and
memory percentiles from historical LeetHub commits are deliberately excluded.
