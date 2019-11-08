"""
Problem 39: Integer right triangles
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
# pylint: disable=invalid-name

from typing import Iterable, Tuple, Sequence


Triangle = Tuple[int, int, int]


def is_right_angle_triangle(triangle: Triangle) -> bool:
    """Check if a given triangle is a right angle triangle."""
    sorted_sides = sorted(triangle)
    return sorted_sides[0]**2 + sorted_sides[1]**2 == sorted_sides[2]**2


def _get_triangles_with_perimeter(p: int) -> Iterable[Triangle]:
    """Get triangles with a given perimeter `p`."""
    for a in range(1, p // 3):
        for b in range(a, ((p - a - 1) // 2) + 1):
            c = p - a - b
            yield (a, b, c)


def _get_integer_right_angle_triangles(threshold: int) -> Iterable[Tuple[int, Sequence[Triangle]]]:
    """Get right angle triangles with integer length sides."""
    for p in range(1, threshold):
        right_angle_triangles = [
            triangle for triangle in _get_triangles_with_perimeter(p) \
                if is_right_angle_triangle(triangle)
        ]
        yield (p, right_angle_triangles)


def main() -> None:
    """Main function."""
    threshold = 1000
    (p, triangles) = max(_get_integer_right_angle_triangles(threshold), key=lambda t: len(t[1]))
    print(f'The number of solutions of right angle triangle with integer length sides is ' \
          f'maximised for a perimeter of {p}. ' \
          f'The number of solutions/triangles for this perimeter is {len(triangles)}.')


if __name__ == '__main__':
    main()
