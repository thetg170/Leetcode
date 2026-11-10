from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0004-median-of-two-sorted-arrays.py"


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [-2, 8], 3.0),
    ],
)
def test_examples(nums1, nums2, expected) -> None:
    assert solution(REFERENCE).findMedianSortedArrays(nums1, nums2) == expected
