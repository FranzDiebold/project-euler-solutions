"""
File utility functions.
"""

from typing import Iterable, List


def get_items_from_file(file_name: str) -> Iterable[str]:
    """Get items as iterable from file with name `file_name`."""
    with open(file_name, 'r') as file_object:
        for line in file_object:
            for item in line.replace('"', '').lower().split(','):
                yield item


def get_line_items_from_file(file_name: str, separator: str = ' ') -> Iterable[List[str]]:
    """Get line items as iterable from file with name `file_name` and separator `separator`."""
    with open(file_name, 'r') as file_object:
        for line in file_object:
            yield line.split(separator)
