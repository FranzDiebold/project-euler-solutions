"""
Problem 4: Largest palindrome product
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
# pylint: disable=stop-iteration-return

from typing import Iterator, Tuple
from heapq import heappush, heappop


def is_palindromic_number(num: int) -> bool:
    """Check if a number is palindromic number."""
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-1 * (i + 1)]:
            return False
    return True


def _get_lower_diagonal_tuples(tuple_sum: int, max_value: int) -> Iterator[Tuple[int, int]]:
    """Get 2-tuples of the lower diagonal for a given tuple sum.

    +---+--------+--------+--------+--------+--------+--------+---+
    |   |   9    |   8    |   7    |   6    |   5    |   4    | … |
    +---+--------+--------+--------+--------+--------+--------+---+
    | 9 | (9, 9) |        |        |        |        |        |   |
    | 8 | (8, 9) | (8, 8) |        |        |        |        |   |
    | 7 | (7, 9) | (7, 8) | (7, 7) |        |        |        |   |
    | 6 | (6, 9) | (6, 8) | (6, 7) | (6, 6) |        |        |   |
    | 5 | (5, 9) | (5, 8) | (5, 7) | (5, 6) | (5, 5) |        |   |
    | 4 | (4, 9) | (4, 8) | (4, 7) | (4, 6) | (4, 5) | (4, 4) |   |
    | … |        |        |        |        |        |        |   |
    +---+--------+--------+--------+--------+--------+--------+---+
    """
    i = tuple_sum // 2
    j = tuple_sum - i
    while i > 0 and j <= max_value:
        yield (i, j)
        i -= 1
        j += 1


def _get_diagonal_tuple_generators(max_value: int) -> Iterator[Iterator[Tuple[int, int]]]:
    """Get diagonal generator for 2-tuple generators."""
    return (_get_lower_diagonal_tuples(tuple_sum, max_value) \
        for tuple_sum in range(2 * max_value, 0, -1))


def get_sorted_number_tuples(number_of_digits: int) -> Iterator[Tuple[int, int]]:
    """Get number 2-tuples with `number_of_digits` digits sorted by their product (descending).

    Example for 1 digit:
    1. (9, 9) -> 81
    2. (8, 9) -> 72
    3. (8, 8) -> 64
    4. (7, 9) -> 63
    ...
    """
    max_value = 10**number_of_digits - 1
    diagonal_tuple_generators = _get_diagonal_tuple_generators(max_value)

    gen = next(diagonal_tuple_generators)
    i, j = next(gen)
    prio_q = []
    heappush(prio_q, (-i*j, ((i, j), gen, True)))
    while prio_q:
        _, item = heappop(prio_q)
        tup, gen, is_new_diagonal = item
        yield tup

        if is_new_diagonal:
            try:
                new_g = next(diagonal_tuple_generators)
                i, j = next(new_g)
                heappush(prio_q, (-i*j, ((i, j), new_g, True)))
            except StopIteration:
                pass

        try:
            i, j = next(gen)
            heappush(prio_q, (-i*j, ((i, j), gen, False)))
        except StopIteration:
            pass


def get_sorted_product_palindromic_number_tuples(
        number_of_digits: int
) -> Iterator[Tuple[int, int]]:
    """Get 2-tuples, whose product is a palindromic number, sorted by their product (descending)."""
    for i, j in get_sorted_number_tuples(number_of_digits):
        if is_palindromic_number(i*j):
            yield (i, j)


def main() -> None:
    """Main function."""
    digits = 3
    sorted_palindromic_numbers = get_sorted_product_palindromic_number_tuples(digits)
    (i, j) = next(sorted_palindromic_numbers)
    largest_palindromic_number = i * j

    print((f'The largest product palindromic number with {digits} digits'
           f' is {largest_palindromic_number:,} ({i:,}, {j:,}).'))


if __name__ == '__main__':
    main()
