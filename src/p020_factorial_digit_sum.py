"""
Problem 20: Factorial digit sum
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from src.common.calculations import calculate_large_factorial


def get_sum_of_digits(number: str) -> int:
    """Get the sum of the digits in a number, i.e. 123 -> 6 (=1+2+3)"""
    return sum([int(digit) for digit in number])


def main() -> None:
    """Main function."""
    factorial_number = 100
    sum_of_digits = get_sum_of_digits(calculate_large_factorial(factorial_number))
    print(f'The sum of the digits in the number {factorial_number:,}! is {sum_of_digits:,}.')


if __name__ == '__main__':
    main()
