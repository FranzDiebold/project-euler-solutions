"""
Problem 14: Longest Collatz sequence
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import pytest


def test_get_collatz_sequence():
    # arrange
    from src.p014_longest_collatz_sequence import get_collatz_sequence

    # act
    actual_collatz_sequence = get_collatz_sequence(13)

    # assert
    expected_collatz_sequence = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    for expected_n in expected_collatz_sequence:
        assert expected_n == next(actual_collatz_sequence)

    with pytest.raises(StopIteration):
        next(actual_collatz_sequence)
