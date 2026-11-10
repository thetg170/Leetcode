from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_counts_duplicate_points_multiplicatively() -> None:
    squares = load_module(REFERENCE).DetectSquares()
    for point in ([3, 10], [11, 2], [3, 2]):
        squares.add(point)
    assert squares.count([11, 10]) == 1
    squares.add([11, 2])
    assert squares.count([11, 10]) == 2
    squares.add([3, 10])
    assert squares.count([11, 10]) == 4


def test_missing_corner_and_non_square_rectangle() -> None:
    squares = load_module(REFERENCE).DetectSquares()
    assert squares.count([0, 0]) == 0
    for point in ([2, 0], [0, 3], [2, 3]):
        squares.add(point)
    assert squares.count([0, 0]) == 0
