"""
String utility functions.
"""


def test_get_alphabetical_value():
    # arrange
    from src.common.strings import get_alphabetical_value

    # act
    actual_result = get_alphabetical_value('COLIN')

    # assert
    expected_result = 53
    assert actual_result == expected_result
