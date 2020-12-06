"""
Problem 62: Cubic permutations
https://projecteuler.net/problem=62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3)
and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import pytest


def test_get_cube_numbers():
    # arrange
    from src.p062_cubic_permutations import get_cube_numbers

    # act
    actual_result = get_cube_numbers()

    # assert
    expected_result = [1, 8, 27, 64, 125, 216, 343]
    for expected_value in expected_result:
        assert expected_value == next(actual_result)


@pytest.mark.parametrize('test_input_number,expected_result', [
    (42, '24'),
    (1337, '1337'),
    (826583, '235688'),
    (9876543210, '0123456789')
])
def test_get_permutation_normal_form(test_input_number, expected_result):
    # arrange
    from src.p062_cubic_permutations import get_permutation_normal_form

    # act
    actual_result = get_permutation_normal_form(test_input_number)

    # assert
    assert expected_result == actual_result


def test_get_sorted_cubic_permutations():
    # arrange
    from src.p062_cubic_permutations import get_sorted_cubic_permutations

    # act
    actual_result = get_sorted_cubic_permutations(3)

    # assert
    expected_result = [41063625, 56623104, 66430125]
    assert expected_result == actual_result
