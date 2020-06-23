"""
Problem 53: Combinatoric selections
https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5 over 3) = 10.

In general, (n over r) = n! / (r! * (n−r)!), where r <= n, n! = n * (n−1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: (23 over 10) = 1144066.

How many, not necessarily distinct, values of (n over r) for 1 <= n <= 100,
are greater than one-million?
"""


def test_get_large_binomial_coefficients():
    # arrange
    from src.p053_combinatoric_selections import get_large_binomial_coefficients

    # act
    actual_result_iter = get_large_binomial_coefficients(100, int(1e6))

    # assert
    expected_result = (23, 10, 1144066)
    assert next(actual_result_iter) == expected_result
