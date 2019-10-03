"""
Problem 21: Amicable numbers
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from typing import Iterable, Tuple

from src.common.divisors import get_sum_of_divisors


def get_amicable_pairs(threshold: int) -> Iterable[Tuple[int, int]]:
    """Get amicable number pairs (as tuples) up to a threshold."""
    number_to_sum_divisors = {}
    for i in range(1, threshold):
        sum_of_divisors = get_sum_of_divisors(i)
        if number_to_sum_divisors.get(sum_of_divisors) == i:
            yield (sum_of_divisors, i)
        number_to_sum_divisors[i] = sum_of_divisors


def main() -> None:
    """Main function."""
    threshold = 10000
    sum_of_amicable_numbers = 0
    # pylint: disable=invalid-name
    for (a, b) in get_amicable_pairs(threshold):
        sum_of_amicable_numbers += a + b
    print(f'The sum of all the amicable numbers under {threshold:,} ' \
          f'is {sum_of_amicable_numbers:,}.')


if __name__ == '__main__':
    main()
