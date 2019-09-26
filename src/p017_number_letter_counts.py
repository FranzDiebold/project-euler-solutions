"""
Problem 17: Number letter counts
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

import re


def _written_out_number_below_one_thousand(number: int) -> str:
    """Get a written out string representation of a given number `number` (below one thousand)."""
    assert number < 1000

    base_numbers_map = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }
    tens_map = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }

    written_out_number = ''

    hundreds = number // 100
    if hundreds > 0:
        written_out_number = base_numbers_map[hundreds] + ' hundred'
    number %= 100

    if number > 0:
        if hundreds > 0:
            written_out_number += ' and '

        tens = number // 10
        if tens >= 2:
            written_out_number += tens_map[tens]
            number %= 10
            if number > 0:
                written_out_number += '-' + base_numbers_map[number]
        else:
            written_out_number += base_numbers_map[number]

    return written_out_number or base_numbers_map[0]


def get_written_out_number(number: int) -> str:
    """Get a written out string representation of a given number `number`.

    Example: 342 -> three hundred and forty-two
    """
    zero = 'zero'
    powers = [
        '',
        'thousand',
        'million',
        'billion',
        'trillion',
        'quadrillion',
        'quintillion',
    ]
    max_number = 10**(len(powers) * 3)

    sign = ''
    if number < 0:
        sign = 'negative '
        number *= -1

    if number > max_number:
        raise ValueError('Number not supported.')

    written_out_number_components = []
    for power_idx, power_name in reversed(list(enumerate(powers))):
        power = 10**(power_idx * 3)
        power_number = number // power
        if power_number:
            number %= power
            written_out_number_components.append(
                _written_out_number_below_one_thousand(power_number)
            )
            if power_name:
                written_out_number_components.append(power_name)

    written_out_number = sign + ' '.join(written_out_number_components)
    return written_out_number or zero


def get_number_of_letters_for_written_out_numbers(
        max_number_inclusive: int
) -> int:
    """Get the number of letters for written out numbers
    from 1 to `max_number_inclusive` (inclusive).
    """
    num_letters = 0
    for i in range(1, max_number_inclusive + 1):
        written_out_number = get_written_out_number(i)
        written_out_number = re.sub(r'[\s-]', '', written_out_number)
        num_letters += len(written_out_number)
    return num_letters


def main() -> None:
    """Main function."""
    max_number_inclusive = 1000
    number_of_letters = get_number_of_letters_for_written_out_numbers(max_number_inclusive)
    print((f'All numbers from 1 to {max_number_inclusive:,} (inclusive) written out in words '
           f'contain {number_of_letters:,} letters.'))


if __name__ == '__main__':
    main()
