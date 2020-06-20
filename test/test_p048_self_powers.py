"""
Problem 48: Self powers
https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def test_get_self_powers():
    # arrange
    from src.p048_self_powers import get_self_powers

    # act
    actual_result_iter = get_self_powers()

    # assert
    expected_result = ['1', '4', '27', '256', '3125', '46656', '823543', '16777216']
    for expected_self_power in expected_result:
        assert next(actual_result_iter) == expected_self_power


def test_get_self_powers_sum():
    # arrange
    from src.p048_self_powers import get_self_powers_sum

    # act
    actual_result = get_self_powers_sum(10)

    # assert
    expected_result = '10405071317'
    assert actual_result == expected_result


def test_get_self_powers_sum_with_last_n_digits_only():
    # arrange
    from src.p048_self_powers import get_self_powers_sum

    # act
    actual_result = get_self_powers_sum(10, 5)

    # assert
    expected_result = '71317'
    assert actual_result.endswith(expected_result)
