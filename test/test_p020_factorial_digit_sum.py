"""
Problem 20: Factorial digit sum
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def test_get_sum_of_digits():
    # arrange
    from src.p020_factorial_digit_sum import get_sum_of_digits

    # act
    actual_result = get_sum_of_digits('3628800')

    # assert
    expected_result = 27
    assert actual_result == expected_result
