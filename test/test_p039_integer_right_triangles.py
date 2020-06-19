"""
Problem 39: Integer right triangles
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import pytest


@pytest.mark.parametrize('test_input_triangle,expected_result', [
    ((20, 48, 52), True),
    ((24, 45, 51), True),
    ((30, 40, 50), True),
    ((19, 49, 52), False),
    ((10, 55, 55), False),
    ((40, 40, 40), False),
])
def test_is_right_angle_triangle(test_input_triangle, expected_result):
    # arrange
    from src.p039_integer_right_triangles import is_right_angle_triangle

    # act
    actual_result = is_right_angle_triangle(test_input_triangle)

    # assert
    assert actual_result == expected_result


def test_get_triangles_with_perimeter():
    # arrange
    from src.p039_integer_right_triangles import _get_triangles_with_perimeter

    # act
    actual_result_iter = _get_triangles_with_perimeter(6)

    # assert
    expected_result = [(1, 1, 4), (1, 2, 3), (2, 2, 2)]
    assert set(actual_result_iter) == set(expected_result)
    # TODO
