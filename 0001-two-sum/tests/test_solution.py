from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0001-two-sum.py"


def test_examples() -> None:
    solver = solution(REFERENCE)
    for nums, target in [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]:
        left, right = solver.twoSum(nums, target)
        assert left != right
        assert nums[left] + nums[right] == target

