"""
Problem 24: Lexicographic permutations
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
    012, 021, 102, 120, 201, 210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# pylint: disable=invalid-name

from typing import Iterable, List, TypeVar
import copy

from src.common.calculations import calculate_product


T = TypeVar('T')


def get_number_of_permutations(items: Iterable[T]) -> int:
    """Get the number of permutations for a given list of items `items`."""
    return calculate_product(range(1, len(items) + 1))


def get_nth_lexicographic_permutation(n: int, sorted_items: List[T]) -> List[T]:
    """Get the `n`-th lexicographic permutation of the sorted items `sorted_items`.

    n is starting a `1`.
    """
    n -= 1
    sorted_items = copy.deepcopy(sorted_items)
    permutation = []
    while sorted_items:
        number_of_permutations = get_number_of_permutations(sorted_items)
        size_of_permutations_groups = number_of_permutations // len(sorted_items)
        idx = n // size_of_permutations_groups
        permutation.append(sorted_items.pop(idx))
        n %= size_of_permutations_groups
    return permutation


def main() -> None:
    """Main function."""
    digits = [str(i) for i in range(10)]
    n = int(1e6)
    permutation = ''.join(get_nth_lexicographic_permutation(n, digits))
    print(f'The {n:,}th lexicographic permutation of {digits} is {permutation}.')


if __name__ == '__main__':
    main()
