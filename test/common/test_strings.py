"""
String utility functions.
"""

import pytest


def test_get_alphabetical_value():
    # arrange
    from src.common.strings import get_alphabetical_value

    # act
    actual_result = get_alphabetical_value('COLIN')

    # assert
    expected_result = 53
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_text,expected_result', [
    ('', 0),
    ('A*k', 214),
])
def test_sum_ascii_values(test_input_text, expected_result):
    # arrange
    from src.common.strings import sum_ascii_values

    # act
    actual_result = sum_ascii_values(test_input_text)

    # assert
    assert actual_result == expected_result
