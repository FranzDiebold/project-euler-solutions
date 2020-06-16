"""
Problem 10: Summation of primes
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from src.common.primes import is_prime


def test_get_sum_of_primes():
    # arrange
    from src.p010_summation_of_primes import get_sum_of_primes

    # act
    actual_result = get_sum_of_primes(10)

    # assert
    expected_result = 17
    assert actual_result == expected_result
