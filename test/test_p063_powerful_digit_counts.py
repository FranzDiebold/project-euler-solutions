"""
Problem 63: Powerful digit counts
https://projecteuler.net/problem=63

The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def test_get_powerful_digits():
    # arrange
    from src.p063_powerful_digit_counts import get_powerful_digits

    # act
    actual_result = get_powerful_digits()

    # assert
    expected_result = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (6, 1),
        (7, 1),
        (8, 1),
        (9, 1),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 2),
        (5, 3),
        (6, 3),
        (7, 3),
        (8, 3),
        (9, 3),
    ]
    for expected_value in expected_result:
        assert expected_value == next(actual_result)
