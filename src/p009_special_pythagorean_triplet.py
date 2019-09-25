"""
Problem 9: Special Pythagorean triplet
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# pylint: disable=invalid-name

from typing import Tuple


def get_special_pythagorean_triplet(triplet_sum: int) -> Tuple[int, int, int]:
    """Get special Pythagorean triplet, for which `a + b + c = triplet_sum`."""
    square_map = {i: i**2 for i in range(1, triplet_sum - 2)}
    for a in range(1, triplet_sum // 3):
        for b in range(a + 1, ((triplet_sum - a - 1) // 2) + 1):
            c = triplet_sum - a - b
            if square_map[a] + square_map[b] == square_map[c]:
                return a, b, c
    raise ValueError(f'No special pythagorean triplet found for sum {triplet_sum}.')


def main() -> None:
    """Main function."""
    triplet_sum = 1000
    a, b, c = get_special_pythagorean_triplet(triplet_sum)
    triplet_product = a * b * c
    print((f'The special pythagorean triplet with the sum {triplet_sum:,} '
           f'is ({a}, {b}, {c}) with the product {triplet_product:,}.'))


if __name__ == '__main__':
    main()
