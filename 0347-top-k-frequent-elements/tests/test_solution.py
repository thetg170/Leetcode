from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0347-top-k-frequent-elements.py"


def test_top_k_frequent() -> None:
    solver = solution(REFERENCE)
    assert set(solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert solver.topKFrequent([1], 1) == [1]
    assert set(solver.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == {-1, 2}

