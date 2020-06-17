"""
Problem 16: Power digit sum
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def test_get_power_of_two():
    # arrange
    from src.p016_power_digit_sum import get_power_of_two

    # act
    actual_result = get_power_of_two(15)

    # assert
    assert actual_result == '32768'


def test_get_sum_of_digits_for_powers_of_two():
    # arrange
    from src.p016_power_digit_sum import get_sum_of_digits_for_powers_of_two

    # act
    actual_result = get_sum_of_digits_for_powers_of_two(15)

    # assert
    assert actual_result == 26
