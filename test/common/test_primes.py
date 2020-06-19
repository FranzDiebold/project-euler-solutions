"""
Prime number utility functions.
"""

import pytest


def test_get_prime_factors():
    # arrange
    from src.common.primes import get_prime_factors

    # act
    expected_prime_factors = [2, 3, 7]
    for idx, prime_factor in enumerate(get_prime_factors(42)):
        #assert
        assert prime_factor == expected_prime_factors[idx]


def test_get_prime_factors_map():
    # arrange
    from src.common.primes import get_prime_factors_map

    # act
    actual_prime_factors_map = get_prime_factors_map(60)
    expected_prime_factors_map = {
        2: 2,
        3: 1,
        5: 1,
    }

    # assert
    assert actual_prime_factors_map == expected_prime_factors_map


@pytest.mark.parametrize('test_input,expected_result', [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (66, False),
    (67, True),
])
def test_is_prime(test_input, expected_result):
    # arrange
    from src.common.primes import is_prime

    # act
    actual_result = is_prime(test_input)

    # assert
    assert actual_result == expected_result, f'Test failed for "{test_input}"'


def test_get_primes_set():
    # arrange
    from src.common.primes import get_primes_set

    # act
    actual_result = get_primes_set(100)

    # assert
    expected_result = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    assert actual_result == expected_result
