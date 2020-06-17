"""
Problem 7: 10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

from src.common.primes import is_prime


def test_get_nth_prime_number():
    # arrange
    from src.p007_10001st_prime import get_nth_prime_number

    # act
    actual_result = get_nth_prime_number(6)

    # assert
    expected_result = 13
    assert actual_result == expected_result
