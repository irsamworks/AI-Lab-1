import heapq


def calculate_path_cost(graph, path):
    """Calculate the cost of a path directly from graph edges."""
    if not path:
        return float("inf")

    total = 0

    for current, next_node in zip(path, path[1:]):
        edge_cost = next(
            (
                cost
                for neighbor, cost in graph.get(current, [])
                if neighbor == next_node
            ),
            None,
        )

        if edge_cost is None:
            raise ValueError(f"Edge {current} -> {next_node} does not exist.")

        total += edge_cost

    return total


def calculate_true_remaining_costs(graph, goal):
    """Calculate shortest remaining costs using reverse edges and UCS."""
    reverse_graph = {}

    for node, edges in graph.items():
        reverse_graph.setdefault(node, [])

        for neighbor, cost in edges:
            reverse_graph.setdefault(neighbor, [])
            reverse_graph[neighbor].append((node, cost))

    distances = {goal: 0}
    queue = [(0, goal)]

    while queue:
        cost, node = heapq.heappop(queue)

        if cost != distances.get(node):
            continue

        for previous, edge_cost in reverse_graph.get(node, []):
            new_cost = cost + edge_cost

            if new_cost < distances.get(previous, float("inf")):
                distances[previous] = new_cost
                heapq.heappush(queue, (new_cost, previous))

    return distances


def audit_heuristic(graph, heuristic, goal):
    """Check heuristic admissibility and edge consistency."""
    true_costs = calculate_true_remaining_costs(graph, goal)

    print("\nHEURISTIC AUDIT")
    print("-" * 55)
    print(f"{'Node':<8}{'h(n)':<8}{'True cost':<12}{'Admissible'}")

    for node in graph:
        true_cost = true_costs.get(node, float("inf"))
        admissible = heuristic[node] <= true_cost

        print(
            f"{node:<8}{heuristic[node]:<8}"
            f"{true_cost:<12}{admissible}"
        )

    consistent = True

    print("\nEdge consistency checks:")

    for node, edges in graph.items():
        for neighbor, edge_cost in edges:
            valid = heuristic[node] <= edge_cost + heuristic[neighbor]

            print(
                f"h({node}) <= {edge_cost} + h({neighbor}): "
                f"{heuristic[node]} <= {edge_cost + heuristic[neighbor]} "
                f"-> {valid}"
            )

            if not valid:
                consistent = False

    print("\nHeuristic admissible:", all(
        heuristic[node] <= true_costs.get(node, float("inf"))
        for node in graph
    ))
    print("Heuristic consistent:", consistent)


def search(graph, heuristic, start, goal, algorithm="astar"):
    """Run A* or UCS and record processed and expanded nodes."""
    priority_queue = []
    counter = 0

    initial_priority = heuristic[start] if algorithm == "astar" else 0

    heapq.heappush(
        priority_queue,
        (initial_priority, counter, 0, start, [start]),
    )

    best_cost = {start: 0}
    processed_nodes = []
    expanded_nodes = []

    while priority_queue:
        priority, _, cost, node, path = heapq.heappop(priority_queue)

        # Ignore stale queue entries.
        if cost != best_cost.get(node):
            continue

        processed_nodes.append(node)

        # The goal is processed but not expanded.
        if node == goal:
            independent_cost = calculate_path_cost(graph, path)

            return {
                "path": path,
                "cost": cost,
                "independent_cost": independent_cost,
                "processed": processed_nodes,
                "expanded": expanded_nodes,
            }

        expanded_nodes.append(node)

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                counter += 1

                if algorithm == "astar":
                    new_priority = new_cost + heuristic[neighbor]
                else:
                    new_priority = new_cost

                heapq.heappush(
                    priority_queue,
                    (
                        new_priority,
                        counter,
                        new_cost,
                        neighbor,
                        path + [neighbor],
                    ),
                )

    return {
        "path": None,
        "cost": float("inf"),
        "independent_cost": float("inf"),
        "processed": processed_nodes,
        "expanded": expanded_nodes,
    }


def display_result(algorithm, result):
    print(f"\nAlgorithm: {algorithm.upper()}")
    print(
        "Path:",
        " -> ".join(result["path"]) if result["path"] else "No path",
    )
    print("Returned cost:", result["cost"])
    print("Independently calculated path cost:", result["independent_cost"])
    print("Processed-node trace:", result["processed"])
    print("Expanded nodes:", result["expanded"])
    print("Expansion count:", len(result["expanded"]))


def main():
    graph = {
        "S": [("A", 1), ("B", 4)],
        "A": [("C", 2)],
        "B": [("G", 5)],
        "C": [("G", 3)],
        "G": [],
    }

    heuristic = {
        "S": 5,
        "A": 4,
        "B": 4,
        "C": 2,
        "G": 0,
    }

    print("LAB 4: INFORMED SEARCH - A* AND UCS")
    print("=" * 55)

    audit_heuristic(graph, heuristic, "G")

    print("\nA* AND UCS COMPARISON")
    print("=" * 55)

    for algorithm in ("astar", "ucs"):
        result = search(graph, heuristic, "S", "G", algorithm)
        display_result(algorithm, result)

    print("\nOVERestimate EXPERIMENT")
    print("=" * 55)

    modified_heuristic = heuristic.copy()
    modified_heuristic["C"] = 10

    print("Original h(C):", heuristic["C"])
    print("Modified h(C):", modified_heuristic["C"])
    print("True remaining cost from C:", 3)

    result = search(
        graph,
        modified_heuristic,
        "S",
        "G",
        "astar",
    )

    display_result("astar with overestimate", result)


if __name__ == "__main__":
    main()