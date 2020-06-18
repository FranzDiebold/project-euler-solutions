"""
Problem 36: Double-base palindromes
http://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import pytest


@pytest.mark.parametrize('test_input_number,expected_result', [
    (1, '1'),
    (2, '10'),
    (3, '11'),
    (4, '100'),
    (5, '101'),
    (6, '110'),
    (7, '111'),
    (42, '101010'),
    (585, '1001001001'),
])
def test_get_number_in_binary(test_input_number, expected_result):
    # arrange
    from src.p036_double_base_palindromes import _get_number_in_binary

    # act
    actual_result = _get_number_in_binary(test_input_number)

    # assert
    assert actual_result == expected_result
