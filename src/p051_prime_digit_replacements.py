"""
Problem 51: Prime digit replacements
https://projecteuler.net/problem=51

By replacing the 1st digit of the 2-digit number *3, it turns out that
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,this 5-digit number
is the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

from typing import Set, Iterable, List, Tuple

from src.common.primes import get_sorted_n_digit_primes
from src.common.numbers import decimal_to_binary


def _get_number_family_primes(number_family: str, primes_set: Set[int]) -> Iterable[int]:
    """
    Get all prime numbers for a given number family `number_family`.
    For example, for `*3` it will yield `13`, `23`, `43`, `53`, `73`, and `83`.
    """
    start_digit = 0 if number_family[0] != '*' else 1
    for i in range(start_digit, 10):
        current_number = int(number_family.replace('*', str(i)))
        if current_number in primes_set:
            yield current_number


def _get_number_family(number_str: str, mask: int) -> str:
    """Get the number family for a given number string `number_str` and a mask `mask`."""
    number_family = ''
    number_str_len = len(number_str)
    for idx, binary_mask in enumerate(decimal_to_binary(mask, number_str_len)):
        number_family += number_str[idx] if binary_mask == '0' else '*'
    return number_family


def _get_number_families(number: int) -> Iterable[str]:
    """Get all number families for a given number `number`."""
    number_str = str(number)
    for i in range(1, pow(2, len(number_str))):
        yield _get_number_family(number_str, i)


def get_target_prime_family(target_prime_family_value: int) -> Tuple[int, str, List[int]]:
    """Get a prime family for a given target value `target_prime_family_value`."""
    number_of_digits = 1
    while True:
        print(f'Checking {number_of_digits} digit numbers...')
        primes_list = get_sorted_n_digit_primes(number_of_digits)
        primes_set = set(primes_list)
        checked_prime_families: Set[str] = set()

        for prime_number in primes_list:
            for prime_family in _get_number_families(prime_number):
                if prime_family not in checked_prime_families:
                    checked_prime_families.add(prime_family)
                    prime_family_primes = list(_get_number_family_primes(prime_family, primes_set))
                    prime_family_value = len(prime_family_primes)
                    if prime_family_value == target_prime_family_value:
                        return prime_family_primes[0], prime_family, prime_family_primes

        number_of_digits += 1


def main() -> None:
    """Main function."""
    target_prime_family_value = 8
    smallest_prime, prime_family, primes = get_target_prime_family(target_prime_family_value)
    print(f'The smallest prime which, by replacing part of the number with the same digit, ' \
          f'is part of an {target_prime_family_value} prime value family is {smallest_prime}.')
    print(f'The prime family is {prime_family} with the primes {primes}.')


if __name__ == '__main__':
    main()
