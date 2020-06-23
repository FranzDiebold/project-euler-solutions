"""
Problem 52: Permuted multiples
https://projecteuler.net/problem=52

It can be seen that the number, 125874, and its double, 251748,contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from typing import Iterable

from src.common.permutations import is_permutation


# pylint: disable=invalid-name
def get_permuted_multiples(multiples: Iterable[int]) -> Iterable[int]:
    """
    Get positive integers, x, such that all multiples in `multiples`
    (i.e. 2x, 3x, 4x, 5x, and 6x), contain the same digits.
    """
    x = 10
    while True:
        is_permuted_multiple = True
        for m in multiples:
            if not is_permutation(x, m*x):
                is_permuted_multiple = False
                break
        if is_permuted_multiple:
            yield x
        x += 1


def main() -> None:
    """Main function."""
    permuted_multiples_iter = get_permuted_multiples([2, 3, 4, 5, 6])
    smallest_permuted_multiple = next(permuted_multiples_iter)
    print(f'The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, ' \
          f'contain the same digits is {smallest_permuted_multiple}.')


if __name__ == '__main__':
    main()
