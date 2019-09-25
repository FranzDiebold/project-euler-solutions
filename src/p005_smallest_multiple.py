"""
Problem 5: Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?
"""

from typing import Dict
from common.primes import get_prime_factors


def _get_prime_factors_map(num: int) -> Dict[int, int]:
    """Get prime factors map.

    For the input number `60`, the output should be:
    ```
    {
        2: 2,
        3: 1,
        5: 1,
    }
    ```
    """
    prime_factors_map = {}
    for prime in get_prime_factors(num):
        prime_factors_map[prime] = prime_factors_map.get(prime, 0) + 1
    return prime_factors_map


def get_smallest_multiple(max_number: int) -> int:
    """Get smallest positive number, that is evenly divisible from `1` to `max_number`."""
    smallest_multiple_prime_factors_map = {}
    for i in range(2, max_number + 1):
        prime_factors_map = _get_prime_factors_map(i)
        for prime, num in prime_factors_map.items():
            smallest_multiple_prime_factors_map[prime] = max(
                smallest_multiple_prime_factors_map.get(prime, 0),
                num
            )

    smallest_multiple = 1
    for prime, num in smallest_multiple_prime_factors_map.items():
        smallest_multiple *= prime**num
    return smallest_multiple


def main() -> None:
    """Main function."""
    max_number = 20
    smallest_multiple = get_smallest_multiple(max_number)
    print(f'The smallest multiple of the numbers from 1 to {max_number} is {smallest_multiple:,}.')


if __name__ == '__main__':
    main()
