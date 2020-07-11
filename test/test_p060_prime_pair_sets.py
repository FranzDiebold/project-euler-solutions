"""
Problem 60: Prime pair sets
https://projecteuler.net/problem=60

The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes
for which any two primes concatenate to produce another prime.
"""


def test_get_directed_prime_pairs():
    # arrange
    from src.p060_prime_pair_sets import get_directed_prime_pairs

    # act
    actual_result_iter = get_directed_prime_pairs()

    # assert
    expected_result = [
        (2, 3),
        (5, 3),
        (7, 3),
        (3, 7),
        (2, 11),
        (11, 3),
        (3, 11),
        (3, 13),
        (13, 7),
        (17, 3),
        (3, 17),
    ]
    for expected_value in expected_result:
        assert next(actual_result_iter) == expected_value


def test_find_max_complete_subgraph_1():
    # arrange
    from src.p060_prime_pair_sets import _find_max_complete_subgraph

    directed_graph = {
        1: {2, 3, 4, 5, 6, 7},
        2: {9},
        3: {1},
        4: {1, 3, 5, 6},
        5: {1, 4, 6, 10},
        6: {1, 4, 5, 8},
        7: {1, 6},
        8: {7},
        9: set(),
        10: {5}
    }
    node = 1

    # act
    actual_result = _find_max_complete_subgraph(directed_graph, node)

    # assert
    expected_result = {1, 4, 5, 6}
    assert actual_result == expected_result


def test_find_max_complete_subgraph_2():
    # arrange
    from src.p060_prime_pair_sets import _find_max_complete_subgraph

    directed_graph = {
        1: {3},
        2: {4},
        3: {2, 4, 5, 6},
        4: {2, 3, 6},
        5: {3, 6, 7, 8},
        6: {3, 5},
        7: {5},
        8: {6},
    }
    node = 3

    # act
    actual_result = _find_max_complete_subgraph(directed_graph, node)

    # assert
    expected_result = {3, 5, 6}
    assert actual_result == expected_result


def test_find_max_complete_subgraph_3():
    # arrange
    from src.p060_prime_pair_sets import _find_max_complete_subgraph

    directed_graph = {
        1: {2, 6},
        2: {1, 3, 6},
        3: {2, 4, 6},
        4: {3, 5, 6},
        5: {4, 6},
        6: {1, 2, 3, 4, 5},
    }
    node = 6

    # act
    actual_result = _find_max_complete_subgraph(directed_graph, node)

    # assert
    expected_result_size = 3
    assert len(actual_result) == expected_result_size
    assert 6 in actual_result


def test_get_prime_pairs_sets():
    # arrange
    from src.p060_prime_pair_sets import get_prime_pairs_sets

    # act
    actual_result_iter = get_prime_pairs_sets(4)

    # assert
    expected_result = {3, 7, 109, 673}
    assert next(actual_result_iter) == expected_result
