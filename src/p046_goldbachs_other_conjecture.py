"""
Problem 46: Goldbach's other conjecture
https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from typing import Iterable
from itertools import count
import math

from src.common.primes import is_prime


def _get_special_odd_composite_numbers() -> Iterable[int]:
    """Get odd composite numbers
    that cannot be written as the sum of a prime and twice a square."""
    primes = {2}
    for odd_number in count(start=3, step=2):
        if is_prime(odd_number):
            primes.add(odd_number)
        else:
            can_be_written_as_sum = False
            for prime_number in primes:
                if math.sqrt((odd_number - prime_number) / 2.0).is_integer():
                    can_be_written_as_sum = True
                    break
            if not can_be_written_as_sum:
                yield odd_number


def main() -> None:
    """Main function."""
    smallest_special_odd_composite_number = next(_get_special_odd_composite_numbers())
    print(f'The smallest odd composite that cannot be written as the sum of a prime ' \
          f'and twice a square is {smallest_special_odd_composite_number:,}.')


if __name__ == '__main__':
    main()
