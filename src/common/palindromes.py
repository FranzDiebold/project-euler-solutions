"""
Palindrome utility functions.
"""

from typing import Union


def is_palindromic_number(number: Union[int, str]) -> bool:
    """Check if a number is palindromic number."""
    number_str = str(number)
    for i in range(len(number_str) // 2):
        if number_str[i] != number_str[-1 * (i + 1)]:
            return False
    return True
