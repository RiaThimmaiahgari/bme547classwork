# test_linear_coordinates.py

import pytest

@pytest.mark.parametrize("tuple1, tuple2, expected", [
    [(3, 2), (1, 4), -1],
    [(5, 6), (4, 3), 3]
    ])
def test_calculate_slope(tuple1, tuple2, expected):
    from linear_coordinates import calculate_slope
    answer = calculate_slope(tuple1, tuple2)
    assert answer == expected


@pytest.mark.parametrize("tuple1, slope, expected", [
    [(3, 2), -1, 5],
    [(5, 6), 3, -9]
    ])
def test_calculate_intercept(tuple1, slope, expected):
    from linear_coordinates import calculate_intercept
    answer = calculate_intercept(tuple1, slope)
    assert answer == expected


@pytest.mark.parametrize("slope, intercept, x_val, expected", [
    [-1, 5, 3, 2],
    [3, -9, 5, 6]
    ])
def test_calculate_yval(slope, intercept, x_val, expected):
    from linear_coordinates import calculate_yval
    answer = calculate_yval(slope, intercept, x_val)
    assert answer == expected
