"""
Number utility functions.
"""

import pytest


@pytest.mark.parametrize('test_input_decimal_number,expected_result', [
    (1, '1'),
    (2, '10'),
    (3, '11'),
    (4, '100'),
    (5, '101'),
    (6, '110'),
    (7, '111'),
    (42, '101010'),
    (585, '1001001001'),
])
def test_decimal_to_binary(test_input_decimal_number, expected_result):
    # arrange
    from src.common.numbers import decimal_to_binary

    # act
    actual_result = decimal_to_binary(test_input_decimal_number)

    # assert
    assert actual_result == expected_result


def test_decimal_to_binary_with_num_digits():
    # arrange
    from src.common.numbers import decimal_to_binary

    # act
    actual_result = decimal_to_binary(5, 6)

    # assert
    expected_result = '000101'
    assert actual_result == expected_result
