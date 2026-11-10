from pathlib import Path

from tests.support.assertions import normalized_nested
from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0078-subsets.py"


def test_all_subsets() -> None:
    solver = solution(REFERENCE)
    actual = solver.subsets([1, 2, 3])
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert normalized_nested(actual) == normalized_nested(expected)
    assert solver.subsets([]) == [[]]

