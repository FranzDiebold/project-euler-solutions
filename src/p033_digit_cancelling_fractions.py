"""
Problem 33: Digit cancelling fractions
http://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from typing import Iterable, Tuple, List

from src.common.primes import get_prime_factors_map


def _get_fractions_less_than_one_in_value(
        num_digits: int
) -> Iterable[Tuple[List[int], List[int]]]:
    """Get fractions of as lists `([4, 9], [9, 8])` with a value less than `1`
    with a given number of digits `num_digits`.
    """
    for denominator_value in range(1, 10**num_digits):
        denominator = tuple((int(digit) for digit in f'{denominator_value}'.rjust(num_digits, '0')))
        for numerator_value in range(0, denominator_value):
            numerator = tuple((int(digit) for digit in f'{numerator_value}'.rjust(num_digits, '0')))
            yield (numerator, denominator)


def _is_non_trivial_fraction(numerator: List[int], denominator: List[int]) -> bool:
    """Check if a given fraction is non-trivial.

    The fraction `30/50 = 3/5` for example is trivial.
    """
    return (numerator[-1] != 0 or denominator[-1] != 0) and \
        (numerator[0] != 0 or denominator[0] != 0)


def _get_incorrectly_simplified_fractions(
        numerator: List[int], denominator: List[int]
) -> Iterable[Tuple[List[int], List[int]]]:
    """Get an incorrectly simplified fraction, if possible.

    Example:
    49/98 -> [4/8]
    12/34 -> []
    """
    for numerator_idx, numerator_digit in enumerate(numerator):
        for denominator_idx, denominator_digit in enumerate(denominator):
            if numerator_digit == denominator_digit:
                simplified_numerator = numerator[:numerator_idx] + numerator[numerator_idx+1:]
                simplified_denominator = denominator[:denominator_idx] + \
                    denominator[denominator_idx+1:]
                yield (simplified_numerator, simplified_denominator)


def _list_of_digits_to_number(list_of_digits: Iterable[int]) -> int:
    """Convert a list of digits to a number."""
    return int(''.join([str(digit) for digit in list_of_digits]))


def _get_correct_incorrectly_simplified_fractions(
        num_digits: int
) -> Iterable[Tuple[Tuple[List[int], List[int]], Tuple[List[int], List[int]]]]:
    """Get mathematically correct tuples of incorrectly simplified fractions.

    Example:
    The fraction 49/98 is such a fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.
    """
    for numerator, denominator in _get_fractions_less_than_one_in_value(num_digits):
        if _is_non_trivial_fraction(numerator, denominator):
            for simplified_numerator, simplified_denominator in \
                _get_incorrectly_simplified_fractions(numerator, denominator):
                numerator_value = float(_list_of_digits_to_number(numerator))
                denominator_value = _list_of_digits_to_number(denominator)
                if denominator_value == 0:
                    continue
                fraction_value = numerator_value / denominator_value

                simplified_numerator_value = float(_list_of_digits_to_number(simplified_numerator))
                simplified_denominator_value = _list_of_digits_to_number(simplified_denominator)
                if simplified_denominator_value == 0:
                    continue
                simplified_fraction_value = simplified_numerator_value / \
                    simplified_denominator_value

                if fraction_value == simplified_fraction_value:
                    yield (
                        (numerator, denominator),
                        (simplified_numerator, simplified_denominator),
                    )


def _simplify_fraction(fraction: Tuple[int, int]) -> Tuple[int, int]:
    """Simplify a fraction `numerator` / `denominator`."""
    numerator, denominator = fraction

    numerator_prime_factors_map = get_prime_factors_map(numerator)
    denominator_prime_factors_map = get_prime_factors_map(denominator)

    simplified_numerator = 1
    for prime, exponent in numerator_prime_factors_map.items():
        simplified_numerator *= prime**(exponent - denominator_prime_factors_map.get(prime, 0))

    simplified_denominator = 1
    for prime, exponent in denominator_prime_factors_map.items():
        simplified_denominator *= prime**(exponent - numerator_prime_factors_map.get(prime, 0))

    return simplified_numerator, simplified_denominator


def main() -> None:
    """Main function."""
    num_digits = 2
    fraction_product = (1, 1)
    for fraction, _ in _get_correct_incorrectly_simplified_fractions(num_digits):
        fraction_product = (
            fraction_product[0] * _list_of_digits_to_number(fraction[0]),
            fraction_product[1] * _list_of_digits_to_number(fraction[1]),
        )
    simplified_fraction_product = _simplify_fraction(fraction_product)
    print(f'The denominator of the product of the curious fractions containing ' \
          f'{num_digits} digits is {simplified_fraction_product[1]:,}.')


if __name__ == '__main__':
    main()
