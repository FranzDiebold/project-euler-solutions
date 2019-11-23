"""
Problem 41: Pandigital prime
https://projecteuler.net/problem=41


We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
# pylint: disable=invalid-name

from typing import Iterable

from src.common.permutations import get_permutations
from src.common.primes import is_prime


def _get_descending_pandigital_prime_numbers() -> Iterable[int]:
    for n in range(9, 0, -1):
        digits = [str(digit) for digit in range(n, 0, -1)]
        for permuted_digits_list in get_permutations(digits):
            permuted_number = int(''.join(permuted_digits_list))
            if is_prime(permuted_number):
                yield permuted_number


def main() -> None:
    """Main function."""
    pandigital_prime = next(_get_descending_pandigital_prime_numbers())
    print(f'The largest n-digit pandigital prime is {pandigital_prime:,}.')


if __name__ == '__main__':
    main()
