"""
Problem 49: Prime permutations
https://projecteuler.net/problem=49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
# pylint: disable=invalid-name

from typing import Iterable, Tuple

from src.common.primes import get_sorted_n_digit_primes
from src.common.permutations import is_permutation


def get_n_digit_prime_arithmetic_sequences(n: int) -> Iterable[Tuple[int]]:
    """
    Get arithmetic sequences made of three increasing numbers which have the following properties:
        (i) each of the three terms are prime, and,
        (ii) each of the 4-digit numbers are permutations of one another, and,
        (iii) they are equidistant.
    """
    n_digit_primes_list = get_sorted_n_digit_primes(n)
    n_digit_primes_set = set(n_digit_primes_list)
    num_n_digit_primes = len(n_digit_primes_list)
    for idx1 in range(num_n_digit_primes):
        prime_1 = n_digit_primes_list[idx1]
        for idx2 in range(idx1 + 1, num_n_digit_primes):
            prime_2 = n_digit_primes_list[idx2]
            prime_3 = prime_2 + (prime_2 - prime_1)
            if prime_3 in n_digit_primes_set and \
                is_permutation(prime_1, prime_2) and \
                is_permutation(prime_2, prime_3):
                yield (prime_1, prime_2, prime_3)


def main() -> None:
    """Main function."""
    n = 4
    arithmetic_sequences = get_n_digit_prime_arithmetic_sequences(n)
    next(arithmetic_sequences)
    relevant_arithmetic_sequence = next(arithmetic_sequences)
    concatenated_number = ''.join([str(number) for number in relevant_arithmetic_sequence])
    print(f'The arithmetic sequence is {relevant_arithmetic_sequence} ' \
          f'and the corresponding 12-digit number is {concatenated_number}.')


if __name__ == '__main__':
    main()
