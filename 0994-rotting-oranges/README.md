Cells hold 0 for empty, 1 for fresh, or 2 for rotten. During each minute, a rotten orange makes each fresh edge-neighbor rotten. Return the number of minutes until none are fresh, or -1 if some can never rot.

## Example

```text
grid = [[2,1,0],[0,1,1]] → 3
```
