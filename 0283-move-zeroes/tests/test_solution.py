from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0283-move-zeroes.py"


def test_moves_zeroes_in_place() -> None:
    solver = solution(REFERENCE)
    nums = [0, 1, 0, 3, 12]
    assert solver.moveZeroes(nums) is None
    assert nums == [1, 3, 12, 0, 0]

    single = [0]
    solver.moveZeroes(single)
    assert single == [0]

