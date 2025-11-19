import pytest
from unittest.mock import patch
from operations import division, multiplication, addition, zero


@patch("operations.randint")
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 25, 27),
        (80, 90, 170),
        (2, 15, -1),
        (90, 90, -1),
    ],
)
def test_addition(mock_randint, a, b, expected):
    mock_randint.return_value = -1
    assert addition(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 25, 0),
        (3, 25, 5),
        (2, 4, 8),
        (13, 27, 1),
    ],
)
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 25, 12),
        (25, 2, 12),
    ],
)
def test_division(a, b, expected):
    assert division(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 8, 0),
        (1, 10, 1),
        (5, 15, 1),
        (2, 25, 2),
        (5, 20, 2),
        (10, 20, 2),
        (10, 25, 2),
        (10, 30, 3),
    ],
)
def test_zero(a, b, expected):
    assert zero(a, b) == expected
