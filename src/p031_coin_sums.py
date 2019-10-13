"""
Problem 31: Coin sums
https://projecteuler.net/problem=31

In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

from typing import Set


def get_number_of_coin_sums(target_sum: int, coins: Set[int]) -> int:
    """Get the number of possible coin sums from a coin set `coins` summing up to `target_sum`."""
    coins = list(sorted(coins))
    count_memo = {0: {-1: 1}}
    for current_sum in range(target_sum + 1):
        for coin_idx, number_of_coin_sums in count_memo.get(current_sum, {}).items():
            for current_coin_idx in range(coin_idx + 1, len(coins)):
                coin = coins[current_coin_idx]

                new_sum = current_sum
                while new_sum < target_sum:
                    new_sum += coin
                    if new_sum not in count_memo:
                        count_memo[new_sum] = {}
                    count_memo[new_sum][current_coin_idx] = count_memo[new_sum].get(current_coin_idx, 0) + number_of_coin_sums
    return sum(count_memo[target_sum].values())


def main() -> None:
    """Main function."""
    coins = set([1, 2, 5, 10, 20, 50, 100, 200])
    target_sum = 200
    number_of_coin_sums = get_number_of_coin_sums(target_sum, coins)
    print(f'The number of different ways {target_sum:,}p can be made ' \
          f'using any number of coins is {number_of_coin_sums:,}.')


if __name__ == '__main__':
    main()
