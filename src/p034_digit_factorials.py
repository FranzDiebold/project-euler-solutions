"""
Problem 34: Digit factorials
http://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from typing import Iterable
import math


def _get_digit_factorials(max_number: int) -> Iterable[int]:
    """Get numbers which are equal to the sum of the factorial of their digits."""
    for number in range(10, max_number):
        digit_factorials = sum(math.factorial(int(digit)) for digit in str(number))
        if digit_factorials == number:
            yield number


def main() -> None:
    """Main function."""
    max_number = int(1e6)
    sum_of_digit_factorials = sum(_get_digit_factorials(max_number))
    print(f'The sum of all numbers which are equal to the sum of the factorial of their digits' \
          f'is {sum_of_digit_factorials:,}.')


if __name__ == '__main__':
    main()
