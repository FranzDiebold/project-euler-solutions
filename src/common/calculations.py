"""
Calculation utility functions.
"""

from typing import Iterable
from functools import reduce
import operator


def calculate_product(numbers: Iterable[int]) -> int:
    """Calculate the product of a given iterable of integer numbers."""
    return reduce(operator.mul, numbers, 1)


def calculate_large_sum(number_strings: Iterable[str]) -> str:
    """Calculate sum of large numbers.

    Args:
        number_strings: iterable of numbers as strings to sum up.
    Returns:
        The sum of the numbers as string.
    """
    large_sum = ''
    new_digit = True
    digit_idx = 1
    remainder = 0
    while new_digit:
        new_digit = False
        current_sum_digit = remainder
        for number in number_strings:
            try:
                digit = int(number[-digit_idx])
                new_digit = True
            except IndexError:
                digit = 0
            current_sum_digit += digit
        large_sum = str(current_sum_digit % 10) + large_sum
        remainder = current_sum_digit // 10
        digit_idx += 1
    if remainder:
        large_sum = str(remainder) + large_sum

    return large_sum.lstrip('0') or '0'


def _multiply_large_number_and_digit(number: str, digit: int) -> str:
    """Multiply a large number (as string) and a digit."""
    large_product = ''
    remainder = 0
    for num_digit in reversed(number):
        current_product_digit = remainder + int(num_digit) * digit
        large_product = str(current_product_digit % 10) + large_product
        remainder = current_product_digit // 10
    if remainder:
        large_product = str(remainder) + large_product
    return large_product


def calculate_large_product(number1: str, number2: str) -> str:
    """Multiply two large numbers given as string. The result will be a string as well."""
    partial_products = []
    for digit_idx, digit_value in enumerate(reversed(number2)):
        partial_product = _multiply_large_number_and_digit(number1, int(digit_value)) + \
            ('0' * digit_idx)
        partial_products.append(partial_product)
    return calculate_large_sum(partial_products)
