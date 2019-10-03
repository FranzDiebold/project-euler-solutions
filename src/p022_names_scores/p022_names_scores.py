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

from typing import Iterable


def get_alphabetical_value(string: str) -> int:
    """Get alphabetical value of a given string `string`.

    Example: 'COLIN' -> 53 = 3 + 15 + 12 + 9 + 14
    """
    return sum([(ord(char) - ord('a') + 1) for char in string.lower()])


def get_names_from_file(file_name: str) -> Iterable[str]:
    """Get names as iterable from file with name `file_name`."""
    with open(file_name, 'r') as file_object:
        for line in file_object:
            for item in line.replace('"', '').lower().split(','):
                yield item


def main() -> None:
    """Main function."""
    file_name = 'p022_names_scores/p022_names.txt'
    total_name_scores = 0
    for idx, name in enumerate(sorted(get_names_from_file(file_name)), 1):
        total_name_scores += idx * get_alphabetical_value(name)
    print(f'The total of all the name scores in the file "{file_name}" is {total_name_scores:,}.')


if __name__ == '__main__':
    main()
