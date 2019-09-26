"""
Problem 10: Summation of primes
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from src.common.primes import is_prime


def get_sum_of_primes(max_prime: int) -> int:
    """Get sum of all prime numbers below `max_prime`."""
    sum_of_primes = 0
    if max_prime >= 3:
        sum_of_primes = 2
        for i in range(3, max_prime, 2):
            if is_prime(i):
                sum_of_primes += i
            if (i - 1) % 1e5 == 0:
                print(f'{i:,} / {max_prime:,} -> {100*i/max_prime:.0f}%')
    return sum_of_primes


def main() -> None:
    """Main function."""
    max_prime = int(2e6)
    print(f'The sum of all prime numbers below {max_prime:,} is {get_sum_of_primes(max_prime):,}.')


if __name__ == '__main__':
    main()
