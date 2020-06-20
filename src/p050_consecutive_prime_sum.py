"""
Problem 50: Consecutive prime sum
https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from typing import List
from copy import copy

from src.common.primes import get_sorted_primes_list


def get_longest_consecutive_prime_sum(threshold: int) -> List[int]:
    """Get the longest sum of consecutive primes that adds to a prime below `threshold`."""
    primes_list = get_sorted_primes_list(threshold)
    primes_set = set(primes_list)
    num_primes = len(primes_list)

    longest_consecutive_primes = []
    for start_idx in range(num_primes):
        current_consecutive_primes = []
        current_sum = 0
        for current_idx in range(start_idx, num_primes):
            current_prime = primes_list[current_idx]
            current_consecutive_primes.append(current_prime)
            current_sum += current_prime

            if current_sum >= threshold:
                break

            if current_sum in primes_set:
                if len(current_consecutive_primes) > len(longest_consecutive_primes):
                    longest_consecutive_primes = copy(current_consecutive_primes)

    return longest_consecutive_primes


def main() -> None:
    """Main function."""
    threshold = int(1e6)
    longest_consecutive_primes = get_longest_consecutive_prime_sum(threshold)
    prime_sum = sum(longest_consecutive_primes)
    print(f'The prime, below one-million, which can be written as ' \
          f'the sum of the most consecutive primes is {prime_sum}.')
    print(f'The {len(longest_consecutive_primes)} consecutive primes ' \
          f'are {longest_consecutive_primes}.')


if __name__ == '__main__':
    main()
