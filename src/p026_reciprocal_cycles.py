"""
Problem 26: Reciprocal cycles
https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	    = 	0.5
1/3	    = 	0.(3)
1/4	    = 	0.25
1/5	    = 	0.2
1/6	    = 	0.1(6)
1/7	    = 	0.(142857)
1/8	    = 	0.125
1/9	    = 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
"""
# pylint: disable=invalid-name

from typing import Tuple


def _calculate_division(
        dividend: int,
        divisor: int,
        max_decimal_places: int = int(1e6)
) -> Tuple[str, str, str]:
    """For given integer `dividend` and `divisor`, calculate the division `dividend / divisor`.
    The decimal fraction part is made up of a fixed starting sequence and a recurring cycle.

    Example:
    1/6 (dividend=1, divisor=6) -> ('0', '1', '6') meaning 0.166666...
    """
    integer_part = str(dividend // divisor)
    remainder = dividend % divisor

    idx = max_decimal_places
    decimal_fraction_parts = []
    while remainder != 0 and len(decimal_fraction_parts) < max_decimal_places:
        remainder *= 10
        decimal_place = str(remainder // divisor)
        remainder %= divisor
        try:
            idx = decimal_fraction_parts.index((decimal_place, remainder))
            break
        except ValueError:
            decimal_fraction_parts.append((decimal_place, remainder))

    decimal_fraction = ''.join(str(decimal_place) for decimal_place, _ in decimal_fraction_parts)
    decimal_fraction_start = decimal_fraction[:idx]
    decimal_fraction_recurring_cycle = decimal_fraction[idx:]
    return integer_part, decimal_fraction_start, decimal_fraction_recurring_cycle


def main() -> None:
    """Main function."""
    threshold_d = 1000
    max_d = None
    _calculate_division(1, 8)
    max_d_recurring_cycle_length = -1
    for d in range(2, threshold_d):
        _, _, recurring_cycle = _calculate_division(1, d)
        if len(recurring_cycle) > max_d_recurring_cycle_length:
            max_d = d
            max_d_recurring_cycle_length = len(recurring_cycle)
    print(f'The unit fraction `1/{max_d:,}` has the longest recurring cycle in its ' \
          f'decimal fraction part of all unit fractions `1/d` for d from 2 to {threshold_d}. ' \
          f'It has a length of {max_d_recurring_cycle_length:,}.')


if __name__ == '__main__':
    main()
