"""
Problem 16: Power digit sum
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from src.common.calculations import calculate_large_sum


def get_power_of_two(exponent: int) -> str:
    """Get the number 2^`exponent` as a string."""
    number = '1'
    for _ in range(exponent):
        number = calculate_large_sum([number, number])
    return number


def get_sum_of_digits_for_powers_of_two(exponent: int) -> int:
    """Get the sum of the digits of the number 2^`exponent`."""
    number = get_power_of_two(exponent)
    return sum([int(digit) for digit in number])


def main() -> None:
    """Main function."""
    exponent = 1000
    print((f'The sum of the digits of the number 2^{exponent} '
           f'is {get_sum_of_digits_for_powers_of_two(exponent):,}.'))


if __name__ == '__main__':
    main()
