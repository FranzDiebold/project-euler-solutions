"""
Problem 15: Lattice paths
https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

import math


def loop_solution(grid_size: int) -> int:
    """Loop solution for number of routes through a `grid_size`x`grid_size`grid."""
    lower_diagonal_matrix = [[1]]
    for i in range(grid_size):
        current_row = lower_diagonal_matrix[i]
        new_row = [1]
        for j in range(1, len(current_row)):
            new_row.append(current_row[j] + new_row[-1])
        new_row.append(2 * new_row[-1])
        lower_diagonal_matrix.append(new_row)
    return lower_diagonal_matrix[-1][-1]


def closed_form_solution(grid_size: int) -> int:
    """Closed form solution for number of routes through a `grid_size`x`grid_size`grid.
    Using binomial coefficents in Pascal's triangle.
    """
    return math.factorial(2 * grid_size) // math.factorial(grid_size)**2


def main() -> None:
    """Main function."""
    grid_size = 20
    print((f'There are {loop_solution(grid_size):,} routes through '
           f'a {grid_size}x{grid_size} grid (loop solution).'))
    print((f'There are {closed_form_solution(grid_size):,} routes through '
           f'a {grid_size}x{grid_size} grid (closed form solution).'))


if __name__ == '__main__':
    main()
