"""
File utility functions.
"""

from typing import Iterable


def get_items_from_file(file_name: str) -> Iterable[str]:
    """Get items as iterable from file with name `file_name`."""
    with open(file_name, 'r') as file_object:
        for line in file_object:
            for item in line.replace('"', '').lower().split(','):
                yield item
