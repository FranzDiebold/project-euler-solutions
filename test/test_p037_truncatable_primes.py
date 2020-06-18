"""
Problem 37: Truncatable primes
http://projecteuler.net/problem=37

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are
both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


def test_get_truncated_numbers():
    # arrange
    from src.p037_truncatable_primes import _get_truncated_numbers

    # act
    actual_result_iter = _get_truncated_numbers(3797)

    # assert
    expected_result = [3797, 379, 37, 3, 797, 97, 7]
    assert set(actual_result_iter) == set(expected_result)
