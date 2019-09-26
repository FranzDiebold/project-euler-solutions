"""
Problem 7: 10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

from src.common.primes import is_prime


def get_nth_prime_number(nth: int) -> int:
    """Get the `nth` prime number."""
    if nth <= 1:
        i = 2
    elif nth == 2:
        i = 3
    else:
        i = 3
        idx = 2
        while idx < nth:
            i += 2
            if is_prime(i):
                idx += 1
    return i


def main() -> None:
    """Main function."""
    prime_idx = 10001
    nth_prime_number = get_nth_prime_number(prime_idx)
    print(f'The {prime_idx:,}th prime number is {nth_prime_number:,}.')


if __name__ == '__main__':
    main()
