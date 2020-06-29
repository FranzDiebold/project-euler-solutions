"""
Problem 57: Square root convergents
https://projecteuler.net/problem=57

It is possible to show that the square root of two can be expressed
as an infinite continued fraction.

sqrt(2) = 1 + (1 / (2 + (1 / (2 + (1 / (2 + ...))))))

By expanding this for the first four iterations, we get:

1 + (1 / 2)                                     = 3 / 2   = 1.5
1 + (1 / (2 + (1 / 2)))                         = 7 / 5   = 1.4
1 + (1 / (2 + (1 / (2 + (1 / 2)))))             = 17 / 12 = 1.41666...
1 + (1 / (2 + (1 / (2 + (1 / (2 + (1 / 2))))))) = 41 / 29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example where the number of digits
in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions,
how many fractions contain a numerator with more digits than the denominator?
"""


def test_get_square_root_expansions():
    # arrange
    from src.p057_square_root_convergents import get_square_root_expansions

    # act
    actual_result_iter = get_square_root_expansions()

    # assert
    expected_result = [
        ('3', '2'),
        ('7', '5'),
        ('17', '12'),
        ('41', '29'),
        ('99', '70'),
        ('239', '169'),
        ('577', '408'),
        ('1393', '985'),
    ]
    for expected_expansion in expected_result:
        assert next(actual_result_iter) == expected_expansion


def test_count_larger_numerator_expansions():
    # arrange
    from src.p057_square_root_convergents import count_larger_numerator_expansions

    # act
    actual_result = count_larger_numerator_expansions(8)

    # assert
    expected_result = 1
    assert actual_result == expected_result
