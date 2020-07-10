"""
Problem 7: 10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

import pytest

from src.common.primes import is_prime


@pytest.mark.parametrize('test_input_nth,expected_result', [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 7),
    (5, 11),
    (6, 13),
])
def test_get_nth_prime_number(test_input_nth, expected_result):
    # arrange
    from src.p007_10001st_prime import get_nth_prime_number

    # act
    actual_result = get_nth_prime_number(test_input_nth)

    # assert
    assert actual_result == expected_result
