"""
Problem 49: Prime permutations
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import pytest


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, []),
    (2, []),
    (3, []),
])
def test_get_n_digit_prime_arithmetic_sequences_no_sequences(test_input_n, expected_result):
    # arrange
    from src.p049_prime_permutations import get_n_digit_prime_arithmetic_sequences

    # act
    actual_result_iter = get_n_digit_prime_arithmetic_sequences(test_input_n)

    # assert
    assert list(actual_result_iter) == expected_result


def test_get_n_digit_prime_arithmetic_sequences_first_4_digit_sequence():
    # arrange
    from src.p049_prime_permutations import get_n_digit_prime_arithmetic_sequences

    # act
    actual_result_iter = get_n_digit_prime_arithmetic_sequences(4)

    # assert
    expected_result = (1487, 4817, 8147)
    assert next(actual_result_iter) == expected_result
