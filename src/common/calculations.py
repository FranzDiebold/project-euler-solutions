"""
Calculation utility functions.
"""

from typing import Iterable


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
