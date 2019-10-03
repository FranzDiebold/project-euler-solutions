"""
Problem 25: 1000-digit Fibonacci number
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from typing import Iterable

from src.common.calculations import calculate_large_sum


def large_fibonacci_numbers() -> Iterable[str]:
    """Fibonnaci numbers generator, returned as strings."""
    f_minus2 = '0'
    f_minus1 = '1'
    while True:
        yield f_minus1
        tmp = f_minus2
        f_minus2 = f_minus1
        f_minus1 = calculate_large_sum([tmp, f_minus2])


def main() -> None:
    """Main function."""
    min_digits = 1000
    idx = -1
    fibonacci_number = '-'
    for idx, fibonacci_number in enumerate(large_fibonacci_numbers(), 1):
        if len(fibonacci_number) >= min_digits:
            break
    print(f'The index of the first term in the Fibonacci sequence to contain {min_digits:,} ' \
          f'digits is {idx:,}.')
    print(f'The Fibonacci number is {fibonacci_number}.')


if __name__ == '__main__':
    main()
