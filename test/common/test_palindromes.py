"""
Palindrome utility functions.
"""

import pytest


@pytest.mark.parametrize('test_input_number,expected_result', [
    (1234, False),
    (121, True),
    ('734437', True),
    (2, True),
    (42421, False),
    (9876, False),
    (3845, False),
    ('7426829', False),
])
def test_is_palindromic_number(test_input_number, expected_result):
    # arrange
    from src.common.palindromes import is_palindromic_number

    # act
    actual_result = is_palindromic_number(test_input_number)

    # assert
    assert actual_result == expected_result
