"""
Permutation utility functions.
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


def get_permutations(sorted_items: List[T]) -> Iterable[List[T]]:
    """Get all permutations of a given list of sorted items `sorted_items`."""
    for n in range(1, get_number_of_permutations(sorted_items) + 1):
        yield get_nth_lexicographic_permutation(n, sorted_items)
