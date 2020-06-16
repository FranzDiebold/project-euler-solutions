"""
Problem 12: Highly divisible triangular number
https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


def test_triangle_number_of_divisors():
    # arrange
    from src.p012_highly_divisible_triangular_number import get_triangle_numbers, get_number_of_divisors

    # act
    triangle_numbers_iter = get_triangle_numbers()

    # assert
    expected_triangle_numbers_and_number_of_divisors = [
        (1, 1),
        (3, 2),
        (6, 4),
        (10, 4),
        (15, 4),
        (21, 4),
        (28, 6),
    ]
    for expected_triangle_number, expected_number_of_divisors in expected_triangle_numbers_and_number_of_divisors:
        actual_triangle_number = next(triangle_numbers_iter)
        assert expected_triangle_number == actual_triangle_number
        assert expected_number_of_divisors == get_number_of_divisors(actual_triangle_number)

