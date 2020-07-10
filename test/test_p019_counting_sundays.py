"""
Problem 19: Counting Sundays
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import pytest


@pytest.mark.parametrize('test_input,expected_result', [
    (1900, False),
    (1901, False),
    (1902, False),
    (1903, False),
    (1904, True),
    (1905, False),
    (1906, False),
    (1907, False),
    (1908, True),
    (2000, True),
])
def test_is_leap_year(test_input, expected_result):
    # arrange
    from src.p019_counting_sundays import is_leap_year

    # act
    actual_result = is_leap_year(test_input)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_month,test_input_year,expected_result', [
    (0, 1900, 31),
    (1, 1900, 28),
    (2, 1900, 31),
    (3, 1900, 30),
    (4, 1900, 31),
    (5, 1900, 30),
    (6, 1900, 31),
    (7, 1900, 31),
    (8, 1900, 30),
    (9, 1900, 31),
    (10, 1900, 30),
    (11, 1900, 31),
    (1, 1904, 29),
])
def test_get_number_of_days_in_month(test_input_month, test_input_year, expected_result):
    # arrange
    from src.p019_counting_sundays import get_number_of_days_in_month

    # act
    actual_result = get_number_of_days_in_month(test_input_month, test_input_year)

    # assert
    assert actual_result == expected_result
