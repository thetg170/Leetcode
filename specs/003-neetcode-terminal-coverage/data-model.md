# Data model

- **Catalog entry** — numbered folder with `problem`, `files`, `classification`,
  and legacy-compatible `review` metadata. New entries reference `starter.py`,
  a skeleton with no implemented methods, and stay outside the legacy kata queue.
- **Statement** — original English Markdown plus a Vietnamese override, both with
  the same sample. The source URL in metadata points to the online problem.
- **Draft** — an unimplemented Python file under the current ignored attempt
  directory. Shared node classes provide structural fields for local use.
- **Anki note** — matched by the existing LeetCode URL and preserved by ID. The
  front gains a command with the exact repository directory. The back and
  scheduling fields stay intact.
