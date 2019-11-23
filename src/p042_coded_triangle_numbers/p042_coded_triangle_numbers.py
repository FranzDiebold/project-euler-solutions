"""
Problem 42: Coded triangle numbers
https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, t_n = 1/2 * n * (n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import math

from src.common.files import get_items_from_file
from src.common.strings import get_alphabetical_value


def is_triangle_number(number: int) -> bool:
    """Check if a given number `number` is a triangle number of the form 1/2 * n * (n+1)."""
    return ((math.sqrt(8*number + 1) - 1) / 2.0).is_integer()


def main() -> None:
    """Main function."""
    file_name = 'src/p042_coded_triangle_numbers/p042_words.txt'
    num_triangle_words = 0
    for word in get_items_from_file(file_name):
        if is_triangle_number(get_alphabetical_value(word)):
            num_triangle_words += 1
    print(f'The number of triangle words in the file "{file_name}" is {num_triangle_words:,}.')


if __name__ == '__main__':
    main()
