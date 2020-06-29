"""
Problem 57: Square root convergents
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed
as an infinite continued fraction.

sqrt(2) = 1 + (1 / (2 + (1 / (2 + (1 / (2 + ...))))))

By expanding this for the first four iterations, we get:

1 + (1 / 2)                                     = 3 / 2   = 1.5
1 + (1 / (2 + (1 / 2)))                         = 7 / 5   = 1.4
1 + (1 / (2 + (1 / (2 + (1 / 2)))))             = 17 / 12 = 1.41666...
1 + (1 / (2 + (1 / (2 + (1 / (2 + (1 / 2))))))) = 41 / 29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example where the number of digits
in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions,
how many fractions contain a numerator with more digits than the denominator?
"""

from typing import Iterable, Tuple

from src.common.calculations import calculate_large_product, calculate_large_sum


def get_square_root_expansions() -> Iterable[Tuple[str, str]]:
    """Get square root expansions for `sqrt(2)` as tuples `(numerator, denominator)`."""
    previous_numerator = '1'
    previous_denominator = '1'
    numerator = '3'
    denominator = '2'
    while True:
        yield numerator, denominator
        numerator, previous_numerator = calculate_large_sum(
            [calculate_large_product(numerator, '2'), previous_numerator]
        ), numerator
        denominator, previous_denominator = calculate_large_sum(
            [calculate_large_product(denominator, '2'), previous_denominator]
        ), denominator


def count_larger_numerator_expansions(threshold: int) -> int:
    """
    Count the number of expansion fractions, where the numerator contains more digits
    than the denominator in the first `threshold` square root expansions.
    """
    square_root_expansions_iter = get_square_root_expansions()
    count = 0
    for _ in range(threshold):
        numerator, denominator = next(square_root_expansions_iter)
        if len(numerator) > len(denominator):
            count += 1
    return count


def main() -> None:
    """Main function."""
    threshold = 1000
    count = count_larger_numerator_expansions(threshold)
    print(f'In the first {threshold:,} expansions, {count:,} fractions contain ' \
          f'a numerator with more digits than the denominator.')


if __name__ == '__main__':
    main()
