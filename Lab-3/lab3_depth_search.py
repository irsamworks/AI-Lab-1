
# Lab 3: Depth-Limited Search (DLS) and Iterative Deepening DFS (IDDFS)

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def dls(start, goal, limit):
    """Return status, path, and visit order for a depth-limited search."""
    visit_order = []

    def recursive_dls(node, path, depth):
        visit_order.append(node)

        if node == goal:
            return "FOUND", path

        if depth == limit:
            # A deeper continuation exists, so the search was cut off.
            if any(neighbor not in path for neighbor in graph[node]):
                return "CUTOFF", None
            return "FAILURE", None

        cutoff_occurred = False

        for neighbor in graph[node]:
            # Path-local cycle check
            if neighbor in path:
                continue

            status, result_path = recursive_dls(
                neighbor, path + [neighbor], depth + 1
            )

            if status == "FOUND":
                return "FOUND", result_path

            if status == "CUTOFF":
                cutoff_occurred = True

        if cutoff_occurred:
            return "CUTOFF", None

        return "FAILURE", None

    status, path = recursive_dls(start, [start], 0)
    return status, path, visit_order


def iddfs(start, goal, max_depth):
    """Run DLS with increasing depth limits from 0 to max_depth."""
    all_visit_orders = []
    limits_attempted = []

    for limit in range(max_depth + 1):
        limits_attempted.append(limit)
        status, path, visit_order = dls(start, goal, limit)
        all_visit_orders.append((limit, visit_order))

        if status == "FOUND":
            return status, path, limits_attempted, all_visit_orders

        if status == "FAILURE":
            # No solution exists within the explored search space.
            return status, None, limits_attempted, all_visit_orders

    return "CUTOFF", None, limits_attempted, all_visit_orders


if __name__ == "__main__":
    print("=== Depth-Limited Search (DLS) ===")

    for limit in [1, 2, 3, 4]:
        status, path, order = dls("A", "G", limit)
        path_text = " -> ".join(path) if path else "None"

        print(f"\nDepth limit: {limit}")
        print("Status:", status)
        print("Path:", path_text)
        print("Visit order:", " -> ".join(order))

    print("\n=== Iterative Deepening DFS (IDDFS) ===")

    for max_depth in [1, 2, 3, 4]:
        status, path, limits, all_orders = iddfs("A", "G", max_depth)
        path_text = " -> ".join(path) if path else "None"

        print(f"\nMaximum depth: {max_depth}")
        print("Status:", status)
        print("Path:", path_text)
        print("Limits attempted:", limits)
