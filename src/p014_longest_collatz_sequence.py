"""
Problem 14: Longest Collatz sequence
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from typing import Iterator, Tuple


def get_collatz_sequence(number: int) -> Iterator[int]:
    """Get Collatz sequence for a given start number `number`."""
    yield number
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        yield number


def get_longest_collatz_sequence_starting_number_and_length(
        starting_number_threshold: int
) -> Tuple[int, int]:
    """Get the starting number and length of the longest Collatz sequence.

    Solution idea: Use memoization.
    """
    length_memoizer = {}

    max_starting_number = None
    max_length = -1
    for starting_number in range(1, starting_number_threshold):
        length = 0
        for number in get_collatz_sequence(starting_number):
            if number in length_memoizer:
                length += length_memoizer[number]
                break
            length += 1
        length_memoizer[starting_number] = length

        if length > max_length:
            max_length = length
            max_starting_number = starting_number

    return max_starting_number, max_length


def main() -> None:
    """Main function."""
    starting_number_threshold = int(1e6)
    max_starting_number, max_length = get_longest_collatz_sequence_starting_number_and_length(
        starting_number_threshold
    )
    print((f'The longest Collatz sequence with a starting number '
           f'under {starting_number_threshold:,} starts with {max_starting_number:,} '
           f'and has a length of {max_length:,}.'))


if __name__ == '__main__':
    main()
