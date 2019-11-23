"""
Problem 40: Champernowne's constant
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If d_n represents the nth digit of the fractional part,
find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""
# pylint: disable=invalid-name

from typing import Iterable


def _get_champernownes_constant_decimal_fraction_digits() -> Iterable[int]:
    """Get single digits from the Champernowne's constant fraction 0.12345678... as an Iterable."""
    i = 1
    while True:
        for digit in str(i):
            yield int(digit)
        i += 1


def _get_product() -> int:
    """Get the value d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000,
    if d_n represents the nth digit of the Champernowne's constant.
    """
    champernownes_constant_digits = _get_champernownes_constant_decimal_fraction_digits()
    product = 1
    n = 1
    for exponent in range(7):
        next_n = 10**exponent
        while n <= next_n:
            d_n = next(champernownes_constant_digits)
            n += 1
        product *= d_n
    return product


def main() -> None:
    """Main function."""
    print(f'The product of the digits is {_get_product():,}.')


if __name__ == '__main__':
    main()
