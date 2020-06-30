"""
Number spiral utilities.

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""

from typing import Iterable, Tuple


def get_spiral_diagonal_values_with_size() -> Iterable[Tuple[int, int]]:
    """
    Get the diagonal values of a number spiral.
    Return tuples of `(<diagonal_value>, <spiral_size>)`.
    """
    value = 1
    current_half_size = 0
    yield value, (2 * current_half_size + 1)
    while True:
        current_half_size += 1
        for _ in range(4):
            value += 2 * current_half_size
            yield value, (2 * current_half_size + 1)


def get_spiral_diagonal_values_up_to_size(size: int) -> Iterable[int]:
    """Get the diagonal values for a `size` by `size` spiral."""
    if size < 1 or size % 2 == 0:
        raise ValueError('The size must be a positive odd number.')

    for current_value, current_size in get_spiral_diagonal_values_with_size():
        if current_size > size:
            break
        yield current_value
