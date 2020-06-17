"""
Problem 30: Digit fifth powers
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import pytest


@pytest.mark.parametrize('test_input_number,expected_result', [
    (1634, True),
    (8208, True),
    (9474, True),
    (1234, False),
    (42, False),
    (9876, False),
    (3827, False),
    (2, False),
])
def test_can_be_written_as_sum_of_nth_power(test_input_number, expected_result):
    # arrange
    from src.p030_digit_fifth_powers import can_be_written_as_sum_of_nth_power

    # act
    actual_result = can_be_written_as_sum_of_nth_power(test_input_number, 4)

    # assert
    assert actual_result == expected_result


def test_get_numbers_that_can_be_written_as_sum_of_nth_power():
    # arrange
    from src.p030_digit_fifth_powers import get_numbers_that_can_be_written_as_sum_of_nth_power

    # act
    actual_result_iter = get_numbers_that_can_be_written_as_sum_of_nth_power(4, int(1e5))

    # assert
    expected_result = [1634, 8208, 9474]
    assert list(actual_result_iter) == expected_result
