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
    number_strings = list(number_strings)
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


def calculate_large_product(number1: str, number2: str, last_n_digits_only: int = 0) -> str:
    """Multiply two large numbers given as string. The result will be a string as well."""
    number1 = number1[-last_n_digits_only:]
    number2 = number2[-last_n_digits_only:]
    partial_products = []
    for digit_idx, digit_value in enumerate(reversed(number2)):
        partial_product = _multiply_large_number_and_digit(number1, int(digit_value)) + \
            ('0' * digit_idx)
        partial_products.append(partial_product)
    return calculate_large_sum(partial_products)[-last_n_digits_only:]


def calculate_large_power(base: int, exponent: int, last_n_digits_only: int = 0) -> str:
    """Calculate `base` to the power of `exponent` for large numbers given as strings."""
    base = str(base)
    power = '1'
    for _ in range(exponent):
        power = calculate_large_product(power, base, last_n_digits_only)[-last_n_digits_only:]
    return power


def calculate_large_factorial(number: int) -> str:
    """Calculate the factorial for a given number `number`.

    Returns:
        factorial: Factorial number as string.
    """
    factorial = '1'
    for i in range(1, number + 1):
        # This would not be needed in Python3 any more, since there is no maximum integer.
        factorial = calculate_large_product(factorial, str(i))
    return factorial


# pylint: disable=invalid-name
def calculate_binomial_coefficient(n: int, k: int) -> int:
    """Calculate the binomial coefficient (n over k)."""
    if n < 0:
        raise ValueError('`n` must not be negative!')
    if k < 0:
        raise ValueError('`k` must not be negative!')
    if k > n:
        return 0

    binomial_coefficient = 1
    for i in range(k):
        binomial_coefficient *= (n - i)
        binomial_coefficient /= (1 + i)
    return round(binomial_coefficient)
