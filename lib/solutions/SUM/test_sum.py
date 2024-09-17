from .sum_solution import sum
import pytest


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (100, 100, 200),
        (0, 100, 100),
        (100, 0, 100),
        (50, 50, 100),
        (99, 1, 100),
        (1, 99, 100),
        (0, 100, 100),
        (100, 0, 100),
        (0, 0, 0),
    ],
)
def test_sum(x, y, expected):
    assert sum(x, y) == expected


@pytest.mark.parametrize(
    "x, y",
    [
        (-1, 2),
        (0, -1),
        (101, 2),
        (0, 101),
    ],
)
def test_sum_fail(x, y):
    with pytest.raises(ValueError):
        sum(x, y)
