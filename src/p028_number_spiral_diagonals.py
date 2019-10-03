"""
Problem 28: Number spiral diagonals
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:

   *21*22 23 24*25*
    20 *7* 8 *9*10
    19  6 *1* 2 11
    18 *5* 4 *3*12
   *17*16 15 14*13*

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from typing import Iterable


def get_spiral_diagonal_values(size: int) -> Iterable[int]:
    """Get the diagonal values for a `size` by `size` spiral."""
    if size < 1 or size % 2 == 0:
        raise ValueError('The size must be a positive odd number.')

    value = 1
    yield value
    for current_size in range(1, (size // 2) + 1):
        for _ in range(4):
            value += 2*current_size
            yield value


def main() -> None:
    """Main function."""
    spiral_size = 1001
    diagonal_sum = sum(get_spiral_diagonal_values(spiral_size))
    print(f'The sum of the numbers on the diagonals in a {spiral_size:,} by {spiral_size:,} ' \
          f'spiral is {diagonal_sum:,}.')


if __name__ == '__main__':
    main()
