"""
Problem 47: Distinct primes factors
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?
"""

from typing import Iterable

from src.common.primes import get_prime_factors_map


def get_distinct_prime_factor_integers(number_of_consecutive_integers: int) -> Iterable[int]:
    """Get `number_of_consecutive_integers` consecutive integers
    which have `number_of_consecutive_integers` distinct prime factors each."""
    consecutive_integers = []

    current_number = 1
    while True:
        number_of_prime_factors = len(get_prime_factors_map(current_number).keys())

        if number_of_prime_factors == number_of_consecutive_integers:
            consecutive_integers.append(current_number)

            if len(consecutive_integers) == number_of_consecutive_integers:
                return consecutive_integers
        else:
            consecutive_integers = []

        current_number += 1


def main() -> None:
    """Main function."""
    number_of_consecutive_integers = 4
    consecutive_integers = get_distinct_prime_factor_integers(number_of_consecutive_integers)
    print(f'The first four consecutive integers to have four distinct prime factors each ' \
          f'are {consecutive_integers}.')


if __name__ == '__main__':
    main()
