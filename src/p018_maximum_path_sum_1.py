"""
Problem 18: Maximum path sum I
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                               75
                              95 64
                            17 47 82
                          18 35 87 10
                        20 04 82 47 65
                      19 01 23 75 03 34
                    88 02 77 73 07 63 67
                  99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
              41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
          70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""

from typing import Iterable, Tuple


def get_maximum_path(tree_level_strings: Iterable[str]) -> Tuple[int, Iterable[int]]:
    """Get maximum path value and maximum path for a given tree, represented as level strings.

    Solution idea: Compute maximum path from *bottom up*. Hence, the time complexity is linear.
    """
    tree_levels = [
        [int(number_string) for number_string in tree_level_string.split()] \
            for tree_level_string in tree_level_strings
    ]

    max_path_tree_levels = [[(value, -1) for value in tree_levels[-1]]]
    for level_idx in range(len(tree_levels) - 2, -1, -1):
        current_tree_level = tree_levels[level_idx]
        previous_path_tree_level = max_path_tree_levels[-1]
        new_path_tree_level = []
        for idx, value in enumerate(current_tree_level):
            left_val = previous_path_tree_level[idx][0]
            right_val = previous_path_tree_level[idx + 1][0]
            if left_val >= right_val:
                new_path_tree_node = (value + left_val, 0)
            else:
                new_path_tree_node = (value + right_val, 1)
            new_path_tree_level.append(new_path_tree_node)
        max_path_tree_levels.append(new_path_tree_level)

    max_path_tree_levels.reverse()

    max_path_tree = []
    node_idx = 0
    for level_idx, level in enumerate(max_path_tree_levels):
        max_path_tree.append(tree_levels[level_idx][node_idx])
        node_idx += level[node_idx][1]

    return max_path_tree_levels[0][0][0], max_path_tree

def main() -> None:
    """Main function."""
    tree_level_strings = (
        '75',
        '95 64',
        '17 47 82',
        '18 35 87 10',
        '20 04 82 47 65',
        '19 01 23 75 03 34',
        '88 02 77 73 07 63 67',
        '99 65 04 28 06 16 70 92',
        '41 41 26 56 83 40 80 70 33',
        '41 48 72 33 47 32 37 16 94 29',
        '53 71 44 65 25 43 91 52 97 51 14',
        '70 11 33 28 77 73 17 78 39 68 17 57',
        '91 71 52 38 17 14 91 43 58 50 27 29 48',
        '63 66 04 68 89 53 67 30 73 16 69 87 40 31',
        '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23',
    )
    max_path_value, max_path = get_maximum_path(tree_level_strings)
    print((f'The maximum total from top to bottom of the triangle is {max_path_value:,}, '
           f'from the path {max_path}.'))


if __name__ == '__main__':
    main()
