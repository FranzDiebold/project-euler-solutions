"""
Problem 35: Circular primes
http://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


def test_get_circular_numbers():
    # arrange
    from src.p035_circular_primes import _get_circular_numbers

    # act
    actual_result_iter = _get_circular_numbers(1234)

    # assert
    expected_result = [1234, 2341, 3412, 4123]
    assert set(actual_result_iter) == set(expected_result)
