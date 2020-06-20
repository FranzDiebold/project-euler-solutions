"""
Calculation utility functions.
"""

import pytest


@pytest.mark.parametrize('test_input_numbers,expected_result', [
    ([42], 42),
    ([3, 12], 36),
    ([1, 2, 3], 6),
    ([4, 7, 0, 1], 0),
])
def test_calculate_product(test_input_numbers, expected_result):
    # arrange
    from src.common.calculations import calculate_product

    # act
    actual_result = calculate_product(test_input_numbers)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_number_strings,expected_result', [
    (['42'], '42'),
    (['3', '12'], '15'),
    (['1', '2', '3'], '6'),
    (['432', '98', '77'], '607'),
])
def test_calculate_large_sum(test_input_number_strings, expected_result):
    # arrange
    from src.common.calculations import calculate_large_sum

    # act
    actual_result = calculate_large_sum(test_input_number_strings)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_number1,test_input_number2,expected_result', [
    ('42', '2', '84'),
    ('876', '927', '812052'),
    ('472983', '0', '0'),
])
def test_calculate_large_product(test_input_number1, test_input_number2, expected_result):
    # arrange
    from src.common.calculations import calculate_large_product

    # act
    actual_result = calculate_large_product(test_input_number1, test_input_number2)

    # assert
    assert actual_result == expected_result


def test_calculate_large_product_with_last_n_digits_only():
    # arrange
    from src.common.calculations import calculate_large_product

    # act
    actual_result = calculate_large_product('7365827', '92890273', 6)

    # assert
    # 7365827 * 92890273 = 684.213.680.900.771
    expected_result = '900771'
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_base,test_input_exponent,expected_result', [
    (2, 3, '8'),
    (42, 2, '1764'),
    (6, 7, '279936'),
])
def test_calculate_large_power(test_input_base, test_input_exponent, expected_result):
    # arrange
    from src.common.calculations import calculate_large_power

    # act
    actual_result = calculate_large_power(test_input_base, test_input_exponent)

    # assert
    assert actual_result == expected_result


def test_calculate_large_power_with_last_n_digits_only():
    # arrange
    from src.common.calculations import calculate_large_power

    # act
    actual_result = calculate_large_power(8, 9, 5)

    # assert
    # 8^9 = 134.217.728
    expected_result = '17728'
    assert actual_result == expected_result
