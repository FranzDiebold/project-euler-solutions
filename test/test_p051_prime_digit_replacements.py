"""
Problem 51: Prime digit replacements
https://projecteuler.net/problem=51

By replacing the 1st digit of the 2-digit number *3, it turns out that
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,this 5-digit number
is the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

import pytest


def test_get_number_family_primes():
    """
    Get all prime numbers for a given number family `number_family`.
    For example, for `*3` it will yield `13`, `23`, `43`, `53`, `73`, and `83`.
    """
    # arrange
    from src.p051_prime_digit_replacements import _get_number_family_primes

    primes_set = {
        2, 3, 5, 7,
        11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    }

    # act
    actual_result_iter = _get_number_family_primes('*3', primes_set)

    # assert
    expected_result = {13, 23, 43, 53, 73, 83}
    assert set(actual_result_iter) == expected_result


@pytest.mark.parametrize('test_input_number_str,test_input_mask,expected_result', [
    ('123', 1, '12*'),
    ('123', 2, '1*3'),
    ('123', 3, '1**'),
    ('123', 4, '*23'),
    ('123', 5, '*2*'),
    ('123', 6, '**3'),
    ('123', 7, '***'),
])
def test_get_number_family(test_input_number_str, test_input_mask, expected_result):
    """Get the number family for a given number string `number_str` and a mask `mask`."""
    # arrange
    from src.p051_prime_digit_replacements import _get_number_family

    # act
    actual_result = _get_number_family(test_input_number_str, test_input_mask)

    # assert
    assert actual_result == expected_result


def test_get_number_families():
    """Get all number families for a given number `number`."""
    # arrange
    from src.p051_prime_digit_replacements import _get_number_families

    # act
    actual_result_iter = _get_number_families(123)

    # assert
    expected_result = { '12*', '1*3', '1**', '*23', '*2*', '**3', '***' }
    assert set(actual_result_iter) == expected_result


@pytest.mark.parametrize('test_input_target_prime_family_value,expected_result', [
    (6, (13, '*3', [13, 23, 43, 53, 73, 83])),
    (7, (56003, '56**3', [56003, 56113, 56333, 56443, 56663, 56773, 56993])),
])
def test_get_target_prime_family(test_input_target_prime_family_value, expected_result):
    """Get a prime family for a given target value `target_prime_family_value`."""
    # arrange
    from src.p051_prime_digit_replacements import get_target_prime_family

    # act
    actual_result = get_target_prime_family(test_input_target_prime_family_value)

    # assert
    assert actual_result == expected_result
