"""
Number utility functions.
"""


def decimal_to_binary(decimal_number: int, num_digits: int = 0) -> str:
    """Get the binary representation of a given decimal number `decimal_number` as string."""
    binary_representation = ''
    while decimal_number > 0:
        binary_representation = str(decimal_number % 2) + binary_representation
        decimal_number //= 2
    return binary_representation.rjust(num_digits, '0')
