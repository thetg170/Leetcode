from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0217-contains-duplicate.py"


def test_duplicate_and_unique_inputs() -> None:
    solver = solution(REFERENCE)
    assert solver.containsDuplicate([1, 2, 3, 1]) is True
    assert solver.containsDuplicate([1, 2, 3, 4]) is False
    assert solver.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

