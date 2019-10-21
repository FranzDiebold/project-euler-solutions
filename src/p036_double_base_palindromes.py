"""
Problem 36: Double-base palindromes
http://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from typing import Iterable

from src.common.palindromes import is_palindromic_number


def _get_number_in_binary(number: int) -> str:
    """Get the binary representation of a given decimal number `number` as string."""
    binary_representation = ''
    while number > 0:
        binary_representation = str(number % 2) + binary_representation
        number //= 2
    return binary_representation


def _get_double_base_palindromes(threshold: int) -> Iterable[int]:
    """Get numbers, which are paldindromic in base 10 and base 2."""
    for number in range(threshold):
        if is_palindromic_number(number) and is_palindromic_number(_get_number_in_binary(number)):
            yield number


def main() -> None:
    """Main function."""
    threshold = int(1e6)
    print(f'The sum of all numbers, less than {threshold:,}, which are palindromic ' \
          f'in base 10 and base 2 is {sum(_get_double_base_palindromes(threshold)):,}.')


if __name__ == '__main__':
    main()
