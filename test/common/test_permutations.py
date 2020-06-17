"""
Permutation utility functions.
"""

import pytest


def test_get_number_of_permutations():
    # arrange
    from src.common.permutations import get_number_of_permutations

    # act
    actual_result = get_number_of_permutations([1, 2, 3, 4])

    # assert
    expected_result = 24
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_n,expected_result', [
    (1, [0, 1, 2]),
    (2, [0, 2, 1]),
    (3, [1, 0, 2]),
    (4, [1, 2, 0]),
    (5, [2, 0, 1]),
    (6, [2, 1, 0]),
])
def test_get_nth_lexicographic_permutation(test_input_n, expected_result):
    # arrange
    from src.common.permutations import get_nth_lexicographic_permutation

    sorted_items = [0, 1, 2]

    # act
    actual_result = get_nth_lexicographic_permutation(test_input_n, sorted_items)

    # assert
    assert actual_result == expected_result


def test_get_permutations():
    # arrange
    from src.common.permutations import get_permutations

    sorted_items = [0, 1, 2]

    # act
    actual_result = get_permutations(sorted_items)

    # assert
    expected_result = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ]
    assert list(actual_result) == expected_result
