"""
Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def loop_solution(threshold: int) -> int:
    """Loop solution."""
    multiple_sum = 0
    for i in range(1, threshold):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i
    return multiple_sum


def closed_form_solution(threshold: int) -> int:
    """Closed form solution."""

    def sum_of_multiples(base: int, threshold: int) -> int:
        number_of_multiples = (threshold - 1) // base
        # using "little Gauss" formula
        return base * ((number_of_multiples * (number_of_multiples + 1)) // 2)

    multiple_sum = sum_of_multiples(3, threshold) + \
        sum_of_multiples(5, threshold) - \
        sum_of_multiples(3*5, threshold)

    return multiple_sum


def main() -> None:
    """Main function."""
    threshold = 1000
    print(f'The loop sum is {loop_solution(threshold):,}.')
    print(f'The closed form sum is {closed_form_solution(threshold):,}.')


if __name__ == '__main__':
    main()
