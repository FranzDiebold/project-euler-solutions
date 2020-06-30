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

from src.common.number_spiral import get_spiral_diagonal_values_up_to_size


def get_spiral_diagonal_values_sum(spiral_size: int) -> int:
    """Get the sum of the numbers on the diagonals in number spiral of size `spiral_size`."""
    return sum(get_spiral_diagonal_values_up_to_size(spiral_size))


def main() -> None:
    """Main function."""
    spiral_size = 1001
    diagonal_sum = get_spiral_diagonal_values_sum(spiral_size)
    print(f'The sum of the numbers on the diagonals in a {spiral_size:,} by {spiral_size:,} ' \
          f'spiral is {diagonal_sum:,}.')


if __name__ == '__main__':
    main()
