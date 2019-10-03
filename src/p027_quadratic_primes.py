"""
Problem 27: Quadratic primes
https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes
for the consecutive integer values 0 <= n <= 39.
However, when n=40,
    40^2 + 40 + 41 = 40 * (40+1) + 41
is divisible by 41, and certainly when n = 41,
    41^2 + 41 + 41
is clearly divisible by 41.

The incredible formula
    n^2 − 79n + 1601
was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n^2 + a*n + b, where |a| < 1000 and |b| <= 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n = 0.
"""
# pylint: disable=invalid-name

from typing import Iterable

from src.common.primes import is_prime


def get_number_sequence(a: int, b: int) -> Iterable[int]:
    """Get an iterable sequence of numbers from the formula n^2 + a*n + b, starting with n = 0."""
    n = 0
    while True:
        yield n**2 + a*n + b
        n += 1


def main() -> None:
    """Main function."""
    max_abs_a = 999
    max_abs_b = 1000

    max_number_of_primes = -1
    max_a_b_tuple = (None, None)
    for a in range(-max_abs_a, max_abs_a + 1):
        for b in range(max_abs_b + 1):
            idx = 0
            for idx, number in enumerate(get_number_sequence(a, b)):
                if not is_prime(number):
                    break
            if idx > max_number_of_primes:
                max_number_of_primes = idx
                max_a_b_tuple = (a, b)
    max_product = max_a_b_tuple[0] * max_a_b_tuple[1]
    print(f'The coefficients {max_a_b_tuple} with the product {max_product:,} produce ' \
          f'the maximum number of {max_number_of_primes:,} primes for consecutive values.')

if __name__ == '__main__':
    main()
