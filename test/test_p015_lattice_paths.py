"""
Problem 15: Lattice paths
https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""


def test_loop_solution():
    # arrange
    from src.p015_lattice_paths import loop_solution

    # act
    actual_result = loop_solution(2)

    # assert
    assert actual_result == 6


def test_closed_form_solution():
    # arrange
    from src.p015_lattice_paths import closed_form_solution

    # act
    actual_result = closed_form_solution(2)

    # assert
    assert actual_result == 6
