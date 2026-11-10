from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0792-binary-search.py"


def test_binary_search() -> None:
    solver = solution(REFERENCE)
    assert solver.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solver.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert solver.search([5], 5) == 0

