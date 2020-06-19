"""
Problem 47: Distinct primes factors
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

import pytest


@pytest.mark.parametrize('test_input_number_of_consecutive_integers,expected_result', [
    (2, [14, 15]),
    (3, [644, 645, 646])
])
def test_get_distinct_prime_factor_integers(test_input_number_of_consecutive_integers, expected_result):
    # arrange
    from src.p047_distinct_primes_factors import get_distinct_prime_factor_integers

    # act
    actual_result_iter = get_distinct_prime_factor_integers(test_input_number_of_consecutive_integers)

    # assert
    assert list(actual_result_iter) == expected_result
