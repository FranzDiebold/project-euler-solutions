"""
Problem 22: Names scores
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from src.common.files import get_items_from_file
from src.common.strings import get_alphabetical_value


def main() -> None:
    """Main function."""
    file_name = 'p022_names_scores/p022_names.txt'
    total_name_scores = 0
    for idx, name in enumerate(sorted(get_items_from_file(file_name)), 1):
        total_name_scores += idx * get_alphabetical_value(name)
    print(f'The total of all the name scores in the file "{file_name}" is {total_name_scores:,}.')


if __name__ == '__main__':
    main()
