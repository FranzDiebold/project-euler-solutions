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

from src.common.permutations import get_nth_lexicographic_permutation


def main() -> None:
    """Main function."""
    digits = [str(i) for i in range(10)]
    n = int(1e6)
    permutation = ''.join(get_nth_lexicographic_permutation(n, digits))
    print(f'The {n:,}th lexicographic permutation of {digits} is {permutation}.')


if __name__ == '__main__':
    main()
