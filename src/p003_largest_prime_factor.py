"""
Problem 3: Largest prime factor
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from src.common.primes import get_prime_factors


def main() -> None:
    """Main function."""
    number = 600851475143
    prime_factors = get_prime_factors(number)
    largest_prime_factor = list(prime_factors)[-1]
    print(f'The largest prime factor of {number:,} is {largest_prime_factor:,}.')


if __name__ == '__main__':
    main()
