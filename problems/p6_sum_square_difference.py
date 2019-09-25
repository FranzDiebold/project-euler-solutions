"""
Problem 6: Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def loop_solution(max_number: int) -> int:
    """Loop solution."""
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, max_number + 1):
        sum_of_squares += i**2
        square_of_sum += i
    square_of_sum = square_of_sum**2
    return square_of_sum - sum_of_squares


def closed_form_solution(max_number: int) -> int:
    """Closed form solution."""
    square_of_sum = (max_number * (max_number + 1) // 2)**2
    sum_of_squares = (max_number * (max_number + 1) * (2 * max_number + 1)) // 6
    return square_of_sum - sum_of_squares


def main() -> None:
    """Main function."""
    max_number = 100
    print((f'The difference for the numbers from 1 to {max_number}'
           f'from loop is {loop_solution(max_number):,}.'))
    print((f'The difference for the numbers from 1 to {max_number}'
           f'from closed form is {closed_form_solution(max_number):,}.'))


if __name__ == '__main__':
    main()
