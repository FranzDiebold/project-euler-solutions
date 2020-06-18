"""
Problem 40: Champernowne's constant
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If d_n represents the nth digit of the fractional part,
find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""


def test_get_champernownes_constant_decimal_fraction_digits():
    # arrange
    from src.p040_champernownes_constant import _get_champernownes_constant_decimal_fraction_digits

    # act
    actual_result_iter = _get_champernownes_constant_decimal_fraction_digits()

    # assert
    expected_result = [
        1, 2, 3, 4, 5, 6, 7, 8, 9,
        1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9,
        2, 0, 2, 1, 2, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9,
        3, 0, 3, 1, 3, 2, 3, 3, 3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9,
        4, 0, 4, 1,
    ]
    for expected_digit in expected_result:
        assert next(actual_result_iter) == expected_digit
