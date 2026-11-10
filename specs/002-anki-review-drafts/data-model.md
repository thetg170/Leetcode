# Data model

- **Problem** — existing catalog entry, identified by its repository directory.
- **Review attempt** — `practice/.lc/reviews/<directory>/attempt-*/solution.py`.
  Created once and kept locally after switching or exiting.
- **Workspace target** — a checkout-relative solution or draft path held by the
  tmux session. Older sessions without this field use the regular solution.
- **Anki card** — the problem title and command on the front, a short recall
  cue or solution outline on the back. Review dates and grades live in Anki.
