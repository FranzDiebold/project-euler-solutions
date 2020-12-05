"""
Special numbers utility functions.
"""

import pytest


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
])
def test_get_triangle_number(test_input_n, expected_result):
    # arrange
    from src.common.special_numbers import get_triangle_number

    # act
    actual_result = get_triangle_number(test_input_n)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_number,expected_result', [
    (0, True),
    (1, True),
    (2, False),
    (3, True),
    (4, False),
    (5, False),
    (6, True),
    (7, False),
    (8, False),
    (9, False),
    (10, True),
    (11, False),
    (377, False),
    (378, True),
])
def test_is_triangle_number(test_input_number, expected_result):
    # arrange
    from src.common.special_numbers import is_triangle_number

    # act
    actual_result = is_triangle_number(test_input_number)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
    (6, 36),
])
def test_get_square_number(test_input_n, expected_result):
    # arrange
    from src.common.special_numbers import get_square_number

    # act
    actual_result = get_square_number(test_input_n)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, 1),
    (2, 5),
    (3, 12),
    (4, 22),
    (5, 35),
    (6, 51),
    (7, 70),
])
def test_get_pentagonal_number(test_input_n, expected_result):
    # arrange
    from src.common.special_numbers import get_pentagonal_number

    # act
    actual_result = get_pentagonal_number(test_input_n)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_number,expected_result', [
    (1, True),
    (2, False),
    (3, False),
    (4, False),
    (5, True),
    (6, False),
    (50, False),
    (51, True),
    (52, False),
    (69, False),
    (70, True),
])
def test_is_pentagonal_number(test_input_number, expected_result):
    # arrange
    from src.common.special_numbers import is_pentagonal_number

    # act
    actual_result = is_pentagonal_number(test_input_number)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, 1),
    (2, 6),
    (3, 15),
    (4, 28),
    (5, 45),
    (6, 66),
    (7, 91),
])
def test_get_hexagonal_number(test_input_n, expected_result):
    # arrange
    from src.common.special_numbers import get_hexagonal_number

    # act
    actual_result = get_hexagonal_number(test_input_n)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_number,expected_result', [
    (1, True),
    (2, False),
    (3, False),
    (4, False),
    (5, False),
    (6, True),
    (7, False),
    (14, False),
    (15, True),
    (16, False),
    (27, False),
    (28, True),
    (29, False),
    (90, False),
    (91, True),
])
def test_is_hexagonal_number(test_input_number, expected_result):
    # arrange
    from src.common.special_numbers import is_hexagonal_number

    # act
    actual_result = is_hexagonal_number(test_input_number)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, 1),
    (2, 7),
    (3, 18),
    (4, 34),
    (5, 55),
])
def test_get_heptagonal_number(test_input_n, expected_result):
    # arrange
    from src.common.special_numbers import get_heptagonal_number

    # act
    actual_result = get_heptagonal_number(test_input_n)

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, 1),
    (2, 8),
    (3, 21),
    (4, 40),
    (5, 65),
])
def test_get_octagonal_number(test_input_n, expected_result):
    # arrange
    from src.common.special_numbers import get_octagonal_number

    # act
    actual_result = get_octagonal_number(test_input_n)

    # assert
    assert actual_result == expected_result
