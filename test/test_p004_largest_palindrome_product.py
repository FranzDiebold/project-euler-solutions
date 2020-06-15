"""
Problem 4: Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def test_get_sorted_product_palindromic_number_tuples():
    # arrange
    from src.p004_largest_palindrome_product import get_sorted_product_palindromic_number_tuples

    # act
    sorted_palindromic_numbers = get_sorted_product_palindromic_number_tuples(2)
    (i, j) = next(sorted_palindromic_numbers)
    actual_result = i * j

    # assert
    excepted_result = 9009
    assert actual_result == excepted_result
