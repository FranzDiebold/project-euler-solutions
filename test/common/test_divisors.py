"""
Proper divisor utility functions.
"""

import pytest


def test_divisors():
    # arrange
    from src.common.divisors import divisors

    # act
    actual_result_iter = divisors(220)

    # assert
    expected_result = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    assert set(actual_result_iter) == set(expected_result)


def test_get_sum_of_divisors():
    # arrange
    from src.common.divisors import get_sum_of_divisors

    # act
    actual_result = get_sum_of_divisors(220)

    # assert
    expected_result = 284
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input,expected_result', [
    (27, False),
    (28, True),
    (29, False),
])
def test_is_perferct_number(test_input, expected_result):
    # arrange
    from src.common.divisors import is_perferct_number

    # act
    actual_result = is_perferct_number(test_input)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input,expected_result', [
    (9, False),
    (10, False),
    (11, False),
    (12, True),
])
def test_is_abundant_number(test_input, expected_result):
    # arrange
    from src.common.divisors import is_abundant_number

    # act
    actual_result = is_abundant_number(test_input)

    # assert
    assert actual_result == expected_result
