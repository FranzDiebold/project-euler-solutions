"""
Problem 30: Digit fifth powers
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import math
from typing import Iterable


def can_be_written_as_sum_of_nth_power(number: int, exponent: int) -> bool:
    """Check if a given integer number `number` can be written
    as the sum of `exponent`th powers of its digits."""
    sum_of_digit_powers = sum([math.pow(int(digit), exponent) for digit in str(number)])
    return number == sum_of_digit_powers


def get_numbers_that_can_be_written_as_sum_of_nth_power(
        exponent: int, max_number: int
) -> Iterable[int]:
    """Get numbers less than `max_number` that
    can be written as the sum of the `exponent`th power as an Iterable."""
    for i in range(10, max_number):
        if can_be_written_as_sum_of_nth_power(i, exponent):
            yield i


def main() -> None:
    """Main function."""
    exponent = 5
    sum_of_numbers = sum(get_numbers_that_can_be_written_as_sum_of_nth_power(exponent, int(1e6)))
    print(f'The sum of all the numbers that can be written as the sum of {exponent}th powers ' \
          f'of their digits is {sum_of_numbers:,}.')


if __name__ == '__main__':
    main()
