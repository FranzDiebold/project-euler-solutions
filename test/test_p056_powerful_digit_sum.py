"""
Problem 56: Powerful digit sum
https://projecteuler.net/problem=56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

import pytest


@pytest.mark.parametrize('test_input_number,expected_result', [
    (42, 6),
    (100000000, 1),
    ('196837', 34),
    ('10677', 21),
])
def test_calculate_digital_sum(test_input_number,expected_result):
    # arrange
    from src.p056_powerful_digit_sum import calculate_digital_sum

    # act
    actual_result = calculate_digital_sum(test_input_number)

    # assert
    assert actual_result == expected_result
