"""
Problem 6: Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def test_loop_solution():
    # arrange
    from src.p006_sum_square_difference import loop_solution

    # act
    actual_result = loop_solution(10)

    # assert
    expected_result = 2640
    assert actual_result == expected_result


def test_closed_form_solution():
    # arrange
    from src.p006_sum_square_difference import closed_form_solution

    # act
    actual_result = closed_form_solution(10)

    # assert
    expected_result = 2640
    assert actual_result == expected_result
