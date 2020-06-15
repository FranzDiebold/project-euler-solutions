"""
Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def test_loop_solution():
    # arrange
    from src.p001_multiples_of_3_and_5 import loop_solution

    # act
    actual_solution = loop_solution(10)

    # assert
    expected_solution = 23
    assert actual_solution == expected_solution


def test_closed_form_solution():
    # arrange
    from src.p001_multiples_of_3_and_5 import closed_form_solution

    # act
    actual_solution = closed_form_solution(10)

    # assert
    expected_solution = 23
    assert actual_solution == expected_solution
