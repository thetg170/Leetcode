Store points as they are added, retaining duplicates. For a query point, count triples of stored point occurrences that form a positive-area, axis-aligned square together with it. The query point does not need to be stored.

## Example

```text
add([2, 0]), add([0, 2]), add([2, 2]), add([2, 2]), count([0, 0]) → 2
```
