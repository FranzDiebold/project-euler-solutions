"""
Problem 55: Lychrel numbers
https://projecteuler.net/problem=55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the reverse and
add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem,
we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either
    (i)  become a palindrome in less than fifty iterations, or,
    (ii) no one, with all the computing power that exists,
         has managed so far to map it to a palindrome.
         In fact, 10677 is the first number to be shown to require over fifty iterations
         before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""

from typing import Optional, Tuple

from src.common.calculations import calculate_large_sum
from src.common.palindromes import is_palindromic_number


def get_number_iterations_to_palindrome(
        number: int,
        max_iterations: int = 50
) -> Optional[Tuple[int, str]]:
    """
    Get the number of iterations to produce a palindrome by adding the number `number`
    with its reverse number.
    Returns a tuple `(<number_of_iterations>, <result_palindrome_number>)`
    or `None` if no palindrome is produced until `max_iterations` iterations.
    """
    number_string = str(number)

    num_iterations = 1
    while num_iterations <= max_iterations:
        number_string = calculate_large_sum((number_string, number_string[::-1]))
        if is_palindromic_number(number_string):
            return num_iterations, number_string
        num_iterations += 1

    return None


def get_number_of_lychrel_numbers(threshold: int, max_iterations: int = 50) -> int:
    """Get the number of Lychrel numbers below `threshold`."""
    number_of_lychrel_numbers = 0
    for number in range(1, threshold):
        if get_number_iterations_to_palindrome(number, max_iterations) is None:
            number_of_lychrel_numbers += 1
    return number_of_lychrel_numbers


def main() -> None:
    """Main function."""
    threshold = 10000
    number_of_lychrel_numbers = get_number_of_lychrel_numbers(threshold, 50)
    print(f'There are {number_of_lychrel_numbers} Lychrel numbers below {threshold:,}.')


if __name__ == '__main__':
    main()
