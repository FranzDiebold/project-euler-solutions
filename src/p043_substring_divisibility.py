"""
Problem 43: Sub-string divisibility
https://projecteuler.net/problem=43

The number 1406357289, is a 0 to 9 pandigital number because
it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:

d_2d_3d_4=406 is divisible by 2
d_3d_4d_5=063 is divisible by 3
d_4d_5d_6=635 is divisible by 5
d_5d_6d_7=357 is divisible by 7
d_6d_7d_8=572 is divisible by 11
d_7d_8d_9=728 is divisible by 13
d_8d_9d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from typing import Iterable

from src.common.permutations import get_permutations


def _get_substring_divisible_pandigital_numbers() -> Iterable[int]:
    """Get all 0 to 9 pandigital numbers with the sub-string divisibility property."""
    pandigital_base_number = [str(digit) for digit in range(0, 10)]
    primes = [2, 3, 5, 7, 11, 13, 17]
    for pandigital_number_list in get_permutations(pandigital_base_number):
        pandigital_number = ''.join(pandigital_number_list)
        is_substring_divisible = True
        for i in range(1, len(pandigital_number) - 2):
            if int(pandigital_number[i:i+3]) % primes[i-1] > 0:
                is_substring_divisible = False
                break
        if is_substring_divisible:
            yield int(pandigital_number)


def main() -> None:
    """Main function."""
    special_pandigital_numbers_sum = sum(_get_substring_divisible_pandigital_numbers())
    print(f'The sum of all 0 to 9 pandigital numbers with ' \
          f'this property is {special_pandigital_numbers_sum:,}.')


if __name__ == '__main__':
    main()
