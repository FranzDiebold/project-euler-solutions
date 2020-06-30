"""
Problem 28: Number spiral diagonals
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:

   *21*22 23 24*25*
    20 *7* 8 *9*10
    19  6 *1* 2 11
    18 *5* 4 *3*12
   *17*16 15 14*13*

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def test_get_spiral_diagonal_values_sum():
    # arrange
    from src.p028_number_spiral_diagonals import get_spiral_diagonal_values_sum

    # act
    actual_result = get_spiral_diagonal_values_sum(5)

    # assert
    expected_result = 101
    assert actual_result == expected_result
