Mutate the room grid so each empty cell stores the shortest number of horizontal or vertical moves to a gate. Walls are -1, gates are 0, and unfilled rooms start at 2147483647. A room that cannot reach a gate keeps the sentinel.

## Example

```text
rooms = [[0,2147483647],[-1,2147483647]] → [[0,1],[-1,2]]
```
