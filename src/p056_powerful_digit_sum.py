"""
Problem 56: Powerful digit sum
https://projecteuler.net/problem=56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

from typing import Union, Tuple

from src.common.calculations import calculate_large_power


def calculate_digital_sum(number: Union[int, str]) -> int:
    """Calculate the digital sum of the number `number`."""
    return sum([int(digit) for digit in str(number)])


# pylint: disable=invalid-name
def get_maximum_power_digital_sum(threshold: int) -> Tuple[int, int, int]:
    """
    Get the maximum digital sum for `a^b`, where `a, b < threshold`.
    Return the tuple `(a, b, <digital_sum_of_a^b>)`.
    """
    max_digital_sum = 0
    max_a, max_b = None, None
    for a in range(1, threshold):
        for b in range(1, threshold):
            power = calculate_large_power(a, b)
            power_digital_sum = calculate_digital_sum(power)
            if power_digital_sum > max_digital_sum:
                max_digital_sum = power_digital_sum
                max_a, max_b = a, b
    return max_a, max_b, max_digital_sum


def main() -> None:
    """Main function."""
    threshold = 100
    max_a, max_b, max_digital_sum = get_maximum_power_digital_sum(threshold)
    print(f'The maximum digital sum is {max_digital_sum:,} for a={max_a} and b={max_b}.')


if __name__ == '__main__':
    main()
