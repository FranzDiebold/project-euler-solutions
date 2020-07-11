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

from typing import Iterable, Tuple, Dict, Set
from collections import defaultdict

from src.common.primes import get_primes, is_prime


def get_directed_prime_pairs() -> Iterable[Tuple[int, int]]:
    """
    Get directed prime pairs `(prime_1, prime_2)`:
    two primes, which by concatenating them
    the result (`<prime_1><prime_2>`) will be prime as well.
    Returns tuples `(prime_1, prime_2)`.
    """
    primes_set = set()
    for new_prime in get_primes():
        for previous_prime in primes_set:
            if is_prime(int(str(new_prime) + str(previous_prime))):
                yield new_prime, previous_prime
            if is_prime(int(str(previous_prime) + str(new_prime))):
                yield previous_prime, new_prime
        primes_set.add(new_prime)


def __find_max_complete_subgraph_recursive(
        directed_graph: Dict[int, Set[int]], relevant_nodes: Set[int], subgraph: Set[int]
) -> Set[int]:
    """Find the maximum complete subgraph."""
    max_complete_subgraph = subgraph
    for current_node in relevant_nodes - subgraph:
        if directed_graph[current_node] >= subgraph:
            all_back_edges = True
            for subgraph_node in subgraph:
                if current_node not in directed_graph[subgraph_node]:
                    all_back_edges = False
                    break
            if all_back_edges:
                current_complete_subgraph = __find_max_complete_subgraph_recursive(
                    directed_graph, relevant_nodes, subgraph | {current_node}
                )
                if len(current_complete_subgraph) > len(max_complete_subgraph):
                    max_complete_subgraph = current_complete_subgraph

    return max_complete_subgraph


def _find_max_complete_subgraph(directed_graph: Dict[int, Set[int]], node: int) -> Set[int]:
    """
    Find the maximum complete subgraph in the given directed graph `directed_graph`,
    in which node `node` is part of.
    """
    relevant_nodes = {
        current_node for current_node in directed_graph[node]
        if node in directed_graph[current_node]
    }
    return __find_max_complete_subgraph_recursive(directed_graph, relevant_nodes, {node})


def get_prime_pairs_sets(size: int) -> Iterable[Set[int]]:
    """
    Get prime pairs sets of size `size`.
    Solution idea: Build a directed graph and search for complete subgraphs of size `size`.
    """
    directed_graph = defaultdict(set)
    for source, sink in get_directed_prime_pairs():
        directed_graph[source].add(sink)
        if source in directed_graph[sink]:
            complete_subgraph = _find_max_complete_subgraph(directed_graph, source)
            if len(complete_subgraph) == size:
                yield complete_subgraph


def main() -> None:
    """Main function."""
    set_size = 5
    prime_pairs_sets = get_prime_pairs_sets(set_size)
    prime_pairs_set = next(prime_pairs_sets)
    print(f'The lowest sum for a set of {set_size} primes for which any two primes ' \
          f'concatenate to produce another prime is {sum(prime_pairs_set)}.')
    print(f'The prime pairs set is {prime_pairs_set}.')


if __name__ == '__main__':
    main()
