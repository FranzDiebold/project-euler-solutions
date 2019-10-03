"""
Problem 23: Non-abundant sums
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers
which cannot be written as the sum of two abundant numbers.
"""

from typing import Set

from src.common.divisors import is_abundant_number


def get_abundant_numbers(threshold: int) -> Set[int]:
    """Get set of abundant numbers below given threshold `threshold'."""
    abundant_numbers = set()
    for i in range(1, threshold + 1):
        if is_abundant_number(i):
            abundant_numbers.add(i)
    return abundant_numbers


def is_sum_of_numbers(number: int, numbers: Set[int]) -> bool:
    """Check if a given number `number` is the sum of any two numbers from `numbers`."""
    for i in range(1, number):
        if i in numbers and (number - i) in numbers:
            return True
    return False


def main() -> None:
    """Main function."""
    threshold = 28123
    total_sum = 0
    abundant_numbers = get_abundant_numbers(threshold)
    for i in range(1, threshold + 1):
        if not is_sum_of_numbers(i, abundant_numbers):
            total_sum += i
    print(f'The sum of all the positive integers which cannot be written as the sum ' \
          f'of two abundant numbers is {total_sum:,}.')


if __name__ == '__main__':
    main()
