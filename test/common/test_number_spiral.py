"""
Number spiral utilities.

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""


def test_get_spiral_diagonal_values_with_size():
    # arrange
    from src.common.number_spiral import get_spiral_diagonal_values_with_size

    # act
    actual_result_iter = get_spiral_diagonal_values_with_size()

    # assert
    expected_result = [
        (1, 1),
        (3, 3),
        (5, 3),
        (7, 3),
        (9, 3),
        (13, 5),
        (17, 5),
        (21, 5),
        (25, 5),
        (31, 7),
        (37, 7),
        (43, 7),
        (49, 7),
    ]
    for expected_value in expected_result:
        assert next(actual_result_iter) == expected_value


def test_get_spiral_diagonal_values_up_to_size():
    # arrange
    from src.common.number_spiral import get_spiral_diagonal_values_up_to_size

    # act
    actual_result_iter = get_spiral_diagonal_values_up_to_size(7)

    # assert
    expected_result = [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
    assert list(actual_result_iter) == expected_result
