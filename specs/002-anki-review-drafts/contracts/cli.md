# CLI contract

- `lc review <problem>` opens a new Python draft. It uses the same selectors
  and optional `--no-attach` argument as `lc open`.
- `lc resume` reopens the active draft if the tmux session still exists.
- `lc run` and `lc test` target the active file. With a problem argument, they
  target the regular solution for that problem. Neovim actions test their
  current buffer after saving it.
- Review drafts are local. Run, Test and Review leave Anki grading to the user.
