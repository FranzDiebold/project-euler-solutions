"""
Problem 32: Pandigital products
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.
"""

from typing import Iterable, Tuple

from src.common.permutations import get_permutations


def _get_pandigital_multiplicand_multiplier_product_tuples(
        max_digit: int
) -> Iterable[Tuple[int, int, int]]:
    """Get multiplicand/multiplier/product tuples,
    which can be written as a 1 through `max_digit` pandigital.
    """
    # pylint: disable=too-many-nested-blocks
    for digits_iter in get_permutations([str(digit) for digit in range(1, max_digit + 1)]):
        digits = ''.join(digits_iter)
        for i in range(1, max_digit - 1):
            for j in range(i + 1, max_digit):
                # length multiplicand:  i
                # length multiplier:    j - i
                # length product:       max_digit - (i + (j - i)) = max_digit - j
                # length of multiplicand * multiplier: (i + (j - i)) = j or j - 1
                # => max_digit - j = j (- 1)
                # => max_digit - 2*j = 0 (- 1)
                if max_digit - 2*j in (0, -1):
                    multiplicand = int(digits[:i])
                    multiplier = int(digits[i:j])
                    if multiplicand < multiplier:
                        product = int(digits[j:])
                        if multiplicand * multiplier == product:
                            yield (multiplicand, multiplier, product)


def main() -> None:
    """Main function."""
    max_digit = 9
    tuples = _get_pandigital_multiplicand_multiplier_product_tuples(max_digit)
    sum_of_products = sum({product for _, _, product in tuples})
    print(f'The sum of all products whose multiplicand/multiplier/product identity ' \
          f'can be written as a 1 through {max_digit} pandigital is {sum_of_products:,}.')


if __name__ == '__main__':
    main()
