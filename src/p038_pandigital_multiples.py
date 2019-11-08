"""
Problem 38: Pandigital multiples
https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
# pylint: disable=invalid-name

from typing import Iterable, Tuple


def is_pandigital(number_str: str) -> bool:
    """Check if a given sequence of numbers are 1 to 9 pandigital."""
    pandigital_number_set = {str(digit) for digit in range(1, 10)}
    return len(number_str) == len(pandigital_number_set) \
        and set(number_str) == pandigital_number_set


def _get_pandigital_multiples() -> Iterable[Tuple[int, int, int]]:
    """Get pandigital multiples."""
    for number in range(1, 98765):
        number_str = str(number)
        for n in range(2, 9):
            number_str += str(n * number)
            if len(number_str) > 9:
                break
            elif len(number_str) < 9:
                continue
            elif is_pandigital(number_str):
                yield (number, n, int(number_str))


def main() -> None:
    """Main function."""
    (number, n, pandigital_number) = max(_get_pandigital_multiples(), key=lambda m: m[2])
    print(f'The largest 1 to 9 pandigital 9-digit number that can be formed as the ' \
          f'concatenated product of an integer with (1,2, ... , n) where n > 1 ' \
          f'is {pandigital_number} ({number}, {n}).')


if __name__ == '__main__':
    main()
