"""
Problem 5: Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?
"""


def test_get_smallest_multiple():
    # arrange
    from src.p005_smallest_multiple import get_smallest_multiple

    # act
    actual_result = get_smallest_multiple(10)

    # assert
    expected_result = 2520
    assert actual_result == expected_result