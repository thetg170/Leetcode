from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0035-search-insert-position.py"


def test_search_and_insertion_positions() -> None:
    solver = solution(REFERENCE)
    assert solver.searchInsert([1, 3, 5, 6], 5) == 2
    assert solver.searchInsert([1, 3, 5, 6], 2) == 1
    assert solver.searchInsert([1, 3, 5, 6], 7) == 4
    assert solver.searchInsert([1, 3, 5, 6], 0) == 0

