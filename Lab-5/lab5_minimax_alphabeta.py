
"""
CAI601400 - Artificial Intelligence Lab
Lab 5: Adversarial Search - Minimax and Alpha-Beta Pruning

Tasks:
1. Trace a game tree using Minimax.
2. Count evaluated leaves in both algorithms.
3. Reorder branches and compare pruning efficiency.
4. Verify that both algorithms return the same Minimax value.
"""

from math import ceil, log2
from typing import List, Optional, Tuple


def minimax(
    scores: List[int],
    depth: int,
    index: int,
    is_max: bool,
    target_depth: int,
    trace: Optional[List[str]] = None,
) -> Tuple[int, int]:
    """Return (best value, number of evaluated leaves)."""

    if depth == target_depth:
        value = scores[index]
        if trace is not None:
            trace.append(f"Evaluate leaf index {index}: value = {value}")
        return value, 1

    left_value, left_count = minimax(
        scores, depth + 1, index * 2, not is_max, target_depth, trace
    )
    right_value, right_count = minimax(
        scores, depth + 1, index * 2 + 1, not is_max, target_depth, trace
    )

    if is_max:
        value = max(left_value, right_value)
        operation = "MAX"
    else:
        value = min(left_value, right_value)
        operation = "MIN"

    if trace is not None:
        trace.append(
            f"{operation} node at depth {depth}, index {index}: "
            f"max/min({left_value}, {right_value}) = {value}"
        )

    return value, left_count + right_count


def alphabeta(
    scores: List[int],
    depth: int,
    index: int,
    is_max: bool,
    target_depth: int,
    alpha: float,
    beta: float,
    trace: Optional[List[str]] = None,
) -> Tuple[int, int]:
    """Return (best value, number of evaluated leaves) using alpha-beta pruning."""

    if depth == target_depth:
        value = scores[index]
        if trace is not None:
            trace.append(f"Evaluate leaf index {index}: value = {value}")
        return value, 1

    evaluated_leaves = 0

    if is_max:
        value = float("-inf")

        for child in range(2):
            child_value, child_count = alphabeta(
                scores,
                depth + 1,
                index * 2 + child,
                False,
                target_depth,
                alpha,
                beta,
                trace,
            )
            evaluated_leaves += child_count
            value = max(value, child_value)
            alpha = max(alpha, value)

            if alpha >= beta:
                if trace is not None:
                    trace.append(
                        f"PRUNE at MAX node index {index}: "
                        f"alpha ({alpha}) >= beta ({beta})"
                    )
                break

    else:
        value = float("inf")

        for child in range(2):
            child_value, child_count = alphabeta(
                scores,
                depth + 1,
                index * 2 + child,
                True,
                target_depth,
                alpha,
                beta,
                trace,
            )
            evaluated_leaves += child_count
            value = min(value, child_value)
            beta = min(beta, value)

            if alpha >= beta:
                if trace is not None:
                    trace.append(
                        f"PRUNE at MIN node index {index}: "
                        f"alpha ({alpha}) >= beta ({beta})"
                    )
                break

    if trace is not None:
        operation = "MAX" if is_max else "MIN"
        trace.append(
            f"{operation} node at depth {depth}, index {index}: "
            f"value = {value}, alpha = {alpha}, beta = {beta}"
        )

    return int(value), evaluated_leaves


def make_complete_tree(values: List[int]) -> Tuple[List[int], int]:
    """Pad values with zeros to make a complete binary tree, as in the manual."""
    target_depth = ceil(log2(len(values))) if len(values) > 1 else 0
    padded = values + [0] * (2**target_depth - len(values))
    return padded, target_depth


def run_comparison(title: str, leaf_values: List[int]) -> None:
    scores, depth = make_complete_tree(leaf_values)

    print(f"\n{title}")
    print("-" * len(title))
    print(f"Leaf values: {leaf_values}")
    print(f"Tree leaf values used: {scores}")
    print(f"Target depth: {depth}")

    minimax_trace: List[str] = []
    minimax_value, minimax_count = minimax(
        scores, 0, 0, True, depth, minimax_trace
    )

    alphabeta_trace: List[str] = []
    alphabeta_value, alphabeta_count = alphabeta(
        scores,
        0,
        0,
        True,
        depth,
        float("-inf"),
        float("inf"),
        alphabeta_trace,
    )

    print("\nMINIMAX TRACE")
    for line in minimax_trace:
        print(line)

    print("\nALPHA-BETA TRACE")
    for line in alphabeta_trace:
        print(line)

    print("\nRESULTS")
    print(f"Minimax root value: {minimax_value}")
    print(f"Minimax evaluated leaves: {minimax_count}")
    print(f"Alpha-Beta root value: {alphabeta_value}")
    print(f"Alpha-Beta evaluated leaves: {alphabeta_count}")
    print(f"Root values agree: {minimax_value == alphabeta_value}")
    print(f"Leaves saved: {minimax_count - alphabeta_count}")

    if minimax_value != alphabeta_value:
        raise AssertionError("Minimax and Alpha-Beta values do not match!")

    if alphabeta_count > minimax_count:
        raise AssertionError("Alpha-Beta evaluated more leaves than Minimax!")


def edge_case_test() -> None:
    """Test a one-leaf tree: root is already terminal."""
    print("\nEDGE-CASE TEST")
    print("---------------")

    scores = [7]
    depth = 0

    mm_value, mm_count = minimax(scores, 0, 0, True, depth)
    ab_value, ab_count = alphabeta(
        scores, 0, 0, True, depth, float("-inf"), float("inf")
    )

    print(f"Single terminal leaf: {scores[0]}")
    print(f"Minimax value/count: {mm_value}/{mm_count}")
    print(f"Alpha-Beta value/count: {ab_value}/{ab_count}")
    print(f"Test passed: {mm_value == ab_value == 7 and mm_count == ab_count == 1}")

    assert mm_value == ab_value == 7
    assert mm_count == ab_count == 1


def main() -> None:
    print("=" * 65)
    print("LAB 5: MINIMAX AND ALPHA-BETA PRUNING")
    print("=" * 65)

    # Manual's supplied Minimax example.
    run_comparison(
        "EXPERIMENT 1: MANUAL'S MINIMAX EXAMPLE",
        [3, 5, 2, 9, 0, 7],
    )

    # Same values, different branch ordering.
    run_comparison(
        "EXPERIMENT 2: REORDERED BRANCHES",
        [0, 7, 3, 5, 2, 9],
    )

    # A complete tree that demonstrates pruning under left-to-right ordering.
    run_comparison(
        "EXPERIMENT 3: PRUNING COMPARISON",
        [3, 5, 2, 9, 3, 5, 2, 9],
    )

    # Reorder leaves to observe a different pruning pattern.
    run_comparison(
        "EXPERIMENT 4: REORDERED EIGHT-LEAF TREE",
        [2, 9, 3, 5, 3, 5, 2, 9],
    )

    edge_case_test()

    print("\nALL TESTS COMPLETED.")


if __name__ == "__main__":
    main()

