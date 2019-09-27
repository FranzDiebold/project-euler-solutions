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

from typing import Iterator, Tuple, Dict


def is_leap_year(year: int) -> bool:
    """Check if a given year `year` is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_number_of_days_in_month(month: int, year: int) -> int:
    """Get the number of days in a given month `month` and `year`

    Args:
        month: 0-11 for Jan-Dec
        year: 4 digit year, i.e. 1974
    Returns:
        The number of days in the given month.
    """
    number_of_days_map = {
        0: 31,  # Jan
        1: 28 + (1 if is_leap_year(year) else 0),  # Feb
        2: 31,  # Mar
        3: 30,  # Apr
        4: 31,  # May
        5: 30,  # Jun
        6: 31,  # Jul
        7: 31,  # Aug
        8: 30,  # Sep
        9: 31,  # Oct
        10: 30,  # Nov
        11: 31,  # Dec
    }
    return number_of_days_map[month]


def get_weekdays_of_first_days_of_months() -> Iterator[Tuple[int, int, int]]:
    """Generator for the weekdays of the first days of months.
    The generator begins with January 1st 1900, which was a Monday.
    The generator yields tuples with the structure: (`year`, `month`, `weekday`).
    `weekday`: Monday is 0 and Sunday is 6.
    """
    weekday = 0
    year = 1900
    while True:
        for month in range(12):
            yield (year, month, weekday)
            weekday = (weekday + get_number_of_days_in_month(month, year)) % 7
        year += 1


def get_weekdays_of_first_days_of_months_map(
        start_year: int, start_month: int, end_year: int, end_month: int
) -> Dict[int, int]:
    """Get the weekdays of the first days of months as map for given time range.

    Only years from 1900 are supported.

    Returns:
        weekdays_of_first_days_of_months_map: {
            0: <number_of_mondays>,
            1: <number_of_tuesdays>,
            ...,
            6: <number_of_sundays>,
        }
    """
    if start_year < 1900:
        raise ValueError('Only years from 1900 are supported.')

    weekdays_of_first_days_of_months_map = {month: 0 for month in range(12)}
    for year, month, weekday in get_weekdays_of_first_days_of_months():
        if year < start_year or (year == start_year and month < start_month):
            continue
        if year > end_year or (year == end_year and month > end_month):
            break
        weekdays_of_first_days_of_months_map[weekday] += 1

    return weekdays_of_first_days_of_months_map


def main() -> None:
    """Main function."""
    start = (1901, 0)
    end = (2000, 11)
    weekdays_of_first_days_of_months_map = get_weekdays_of_first_days_of_months_map(
        start[0], start[1], end[0], end[1]
    )
    print((f'Between {start} and {end} {weekdays_of_first_days_of_months_map[6]} Sundays '
           'fell on the first of the month.'))


if __name__ == '__main__':
    main()
