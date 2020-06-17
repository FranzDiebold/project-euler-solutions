"""
Problem 26: Reciprocal cycles
https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	    = 	0.5
1/3	    = 	0.(3)
1/4	    = 	0.25
1/5	    = 	0.2
1/6	    = 	0.1(6)
1/7	    = 	0.(142857)
1/8	    = 	0.125
1/9	    = 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
"""

import pytest


@pytest.mark.parametrize('test_input_divisor,expected_result', [
    (2, ('0', '5', '')),
    (3, ('0', '', '3')),
    (4, ('0', '25', '')),
    (5, ('0', '2', '')),
    (6, ('0', '1', '6')),
    (7, ('0', '', '142857')),
    (8, ('0', '125', '')),
    (9, ('0', '', '1')),
    (10, ('0', '1', '')),
])
def test_calculate_division(test_input_divisor, expected_result):
    # arrange
    from src.p026_reciprocal_cycles import _calculate_division

    # act
    actual_result = _calculate_division(1, test_input_divisor)

    # assert
    assert actual_result == expected_result
