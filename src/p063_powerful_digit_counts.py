"""
Problem 63: Powerful digit counts
https://projecteuler.net/problem=63

The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from typing import Iterator, Tuple


def get_powerful_digits() -> Iterator[Tuple[int, int]]:
    """Get the number of n-digit positive integers which are also an nth power."""
    power = 1
    found = True
    while found is True:
        base = 1
        found = False
        while len(str(pow(base, power))) <= power:
            if len(str(pow(base, power))) == power:
                yield (base, power)
                found = True
            base += 1
        power += 1


def get_powerful_digit_counts() -> int:
    """Get the number of n-digit positive integers which are also an nth power."""
    return sum(1 for _ in get_powerful_digits())


def main() -> None:
    """Main function."""
    powerful_digit_counts = get_powerful_digit_counts()

    print('The number of n-digit positive integers '
          f'which are also an nth power is {powerful_digit_counts}.')


if __name__ == '__main__':
    main()
