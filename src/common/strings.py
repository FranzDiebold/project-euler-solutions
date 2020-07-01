"""
String utility functions.
"""


def get_alphabetical_value(string: str) -> int:
    """Get alphabetical value of a given string `string`.

    Example: 'COLIN' -> 53 = 3 + 15 + 12 + 9 + 14
    """
    return sum([(ord(char) - ord('a') + 1) for char in string.lower()])


def sum_ascii_values(text: str) -> int:
    """Sum the ASCII values of the given text `text`."""
    return sum(ord(character) for character in text)
