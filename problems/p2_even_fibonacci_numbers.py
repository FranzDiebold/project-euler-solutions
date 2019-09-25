"""
Problem 2: Even Fibonacci numbers
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fibonacci_numbers():
    """Fibonacci numbers generator."""
    f_minus2 = 0
    f_minus1 = 1
    while True:
        yield f_minus2 + f_minus1
        tmp = f_minus2
        f_minus2 = f_minus1
        f_minus1 = tmp + f_minus2


def get_even_fibonacci_numbers_sum(threshold: int) -> int:
    """Get sum of even Fibonacci numbers below `threshold`."""
    fib_sum = 0
    for fib in fibonacci_numbers():
        if fib > threshold:
            break
        # random fact: every third fibonacci number is even
        if fib % 2 == 0:
            fib_sum += fib
    return fib_sum


def main() -> None:
    """Main function."""
    threshold = int(4e6)
    print((f'The sum of even Fibonacci numbers below {threshold:,} '
           f'is {get_even_fibonacci_numbers_sum(threshold):,}.'))


if __name__ == '__main__':
    main()
