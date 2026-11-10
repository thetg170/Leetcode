from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        pytest.param(
            [1, 1, 2, 4, 5],
            6,
            [[1, 1, 4], [1, 5], [2, 4]],
            id="duplicates-are-allowed-only-by-multiplicity",
        ),
        pytest.param([2], 4, [], id="cannot-reuse-a-candidate"),
        pytest.param([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]], id="unique-combinations"),
    ],
)
def test_cases(candidates: list[int], target: int, expected: list[list[int]]) -> None:
    actual = solution(REFERENCE).combinationSum2(candidates, target)
    assert sorted(sorted(combination) for combination in actual) == sorted(expected)
