"""
Problem 52: Permuted multiples
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748,contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def test_get_permuted_multiples():
    # arrange
    from src.p052_permuted_multiples import get_permuted_multiples

    # act
    actual_result_iter = get_permuted_multiples([2])

    # assert
    expected_result = 125874
    assert next(actual_result_iter) == expected_result
