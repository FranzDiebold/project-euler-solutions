"""
Problem 58: Spiral primes
https://projecteuler.net/problem=58

Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral
for which the ratio of primes along both diagonals first falls below 10%?
"""

from typing import Iterable, Tuple

from src.common.number_spiral import get_spiral_diagonal_values_with_size
from src.common.primes import is_prime


def get_spiral_diagonal_prime_ratios() -> Iterable[Tuple[int, int, int]]:
    """
    For increasing number spiral sizes get the ratios of primes along the diagonals.
    Returns tuples `(<spiral_size>, <number_of_primes_along_diagonals>, <diagonal_numbers_count>)`.
    """
    number_of_primes = 0
    total_number = 0
    for value, size in get_spiral_diagonal_values_with_size():
        total_number += 1
        if value == size * size:
            yield size, number_of_primes, total_number
        else:
            if is_prime(value):
                number_of_primes += 1


def main() -> None:
    """Main function."""
    threshold_inverse = 10
    spiral_diagonal_prime_ratios_iter = get_spiral_diagonal_prime_ratios()
    next(spiral_diagonal_prime_ratios_iter)
    for size, number_of_primes, total_number in spiral_diagonal_prime_ratios_iter:
        if number_of_primes * threshold_inverse < total_number:
            print(f'The side length of the square spiral for which the ratio of primes ' \
                  f'along both diagonals first falls below 10% is {size:,}.')
            print(f'This ratio is {number_of_primes:,} / {total_number:,}.')
            break


if __name__ == '__main__':
    main()
