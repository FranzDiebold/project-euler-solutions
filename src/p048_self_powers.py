"""
Problem 48: Self powers
https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from typing import Iterable
import itertools

from src.common.calculations import calculate_large_power, calculate_large_sum


# pylint: disable=invalid-name
def get_self_powers(last_n_digits_only: int = 0) -> Iterable[str]:
    """Get increasing self powers `n^n` (`1^1`, `2^2`, ...) as an Iterable."""
    n = 1
    while True:
        yield calculate_large_power(n, n, last_n_digits_only)
        n += 1


def get_self_powers_sum(max_n: int, last_n_digits_only: int = 0) -> str:
    """Get the series, `1^1 + 2^2 + ... + max_n^max_n`."""
    return calculate_large_sum(itertools.islice(get_self_powers(last_n_digits_only), max_n))


def main() -> None:
    """Main function."""
    max_n = 1000
    last_n_digits_only = 10
    self_powers_sum = get_self_powers_sum(max_n, last_n_digits_only)
    print(f'The last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 ' \
          f'are {self_powers_sum[-last_n_digits_only:]}.')


if __name__ == '__main__':
    main()
