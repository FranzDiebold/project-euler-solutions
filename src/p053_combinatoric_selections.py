"""
Problem 53: Combinatoric selections
https://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5 over 3) = 10.

In general, (n over r) = n! / (r! * (n−r)!), where r <= n, n! = n * (n−1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: (23 over 10) = 1144066.

How many, not necessarily distinct, values of (n over r) for 1 <= n <= 100,
are greater than one-million?
"""

from typing import Iterable, Tuple

from src.common.calculations import calculate_binomial_coefficient


# pylint: disable=invalid-name
def get_large_binomial_coefficients(max_n: int, threshold: int) -> Iterable[Tuple[int, int, int]]:
    """
    Get binomial coefficients (n over r) for `1 <= n <= max_n` that are greater than `threshold`.
    Returns tuples `(n, r, (n over r))`.
    """
    for n in range(1, max_n + 1):
        for r in range(n + 1):
            binomial_coefficient = calculate_binomial_coefficient(n, r)
            if binomial_coefficient > threshold:
                yield n, r, binomial_coefficient


def main() -> None:
    """Main function."""
    max_n = 100
    threshold = int(1e6)
    count = len(list(get_large_binomial_coefficients(max_n, threshold)))
    print(f'The number of values of (n over r) for 1 <= n <= {max_n} ' \
          f'that are greater than {threshold:,} is {count}.')


if __name__ == '__main__':
    main()
