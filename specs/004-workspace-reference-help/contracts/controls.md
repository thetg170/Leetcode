# Controls contract

- `Space l s` shows the local archived solution from the selected code buffer.
- `Space l h` shows the keyboard table. `q` and `Esc` close either view.
- `lc reference [problem]` prints the local archived path if available.
  The editor passes its exact buffer through the internal `--path` option.
- `Space l t` still saves and runs the curated tests. `Ctrl+Space` then `d`
  detaches, and `lc resume` reattaches.
