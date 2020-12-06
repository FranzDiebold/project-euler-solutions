"""
Problem 62: Cubic permutations
https://projecteuler.net/problem=62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3)
and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from typing import Iterable, Iterator
from collections import defaultdict


def get_cube_numbers() -> Iterator[int]:
    """Get cube numbers 1, 8, 27, ... as a generator."""
    idx = 1
    while True:
        yield idx**3
        idx += 1


def get_permutation_normal_form(number: int) -> str:
    """Get the permutation normal form of a given number 'number'."""
    return ''.join(sorted(list(str(number))))


# pylint: disable=inconsistent-return-statements
def get_sorted_cubic_permutations(num_permutations: int) -> Iterable[int]:
    """Get sorted cubic permutations."""
    normal_form_to_numbers_map = defaultdict(list)
    for number in get_cube_numbers():
        permutation_normal_form = get_permutation_normal_form(number)
        normal_form_to_numbers_map[permutation_normal_form].append(number)
        if len(normal_form_to_numbers_map[permutation_normal_form]) == num_permutations:
            return normal_form_to_numbers_map[permutation_normal_form]


def main() -> None:
    """Main function."""
    num_permutations = 5

    sorted_cubic_permutations = get_sorted_cubic_permutations(num_permutations)
    print(f'The smallest cube for which exactly {num_permutations} permutations ' \
          f'of its digits are cube is {sorted_cubic_permutations[0]}.')
    print(f'All permutations are {sorted_cubic_permutations}.')


if __name__ == '__main__':
    main()
