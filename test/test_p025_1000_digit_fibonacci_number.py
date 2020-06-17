"""
Problem 25: 1000-digit Fibonacci number
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def test_large_fibonacci_numbers():
    # arrange
    from src.p025_1000_digit_fibonacci_number import large_fibonacci_numbers

    # act
    actual_result_iter = large_fibonacci_numbers()

    # assert
    expected_result = ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89', '144']
    for expected_f in expected_result:
        assert expected_f == next(actual_result_iter)
