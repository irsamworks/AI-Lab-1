
import heapq
from collections import deque

# Weighted graph for the Task 3 experiment.
# The C -> G corridor is the added alternative route.

weighted_graph = {
    "A": [("B", 1), ("C", 1)],
    "B": [("D", 1), ("E", 1)],
    "C": [("F", 1), ("G", 11)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}


def ucs(start, goal):
    # Priority queue entries: (total_cost, tie_breaker, node, path)
    frontier = [(0, 0, start, [start])]
    counter = 1
    best_cost = {start: 0}
    visit_order = []

    while frontier:
        cost, _, node, path = heapq.heappop(frontier)

        # Ignore outdated entries in the priority queue.
        if cost > best_cost.get(node, float("inf")):
            continue

        visit_order.append(node)

        # Stop when the goal is processed.
        if node == goal:
            return path, cost, visit_order

        for neighbor, edge_cost in weighted_graph[node]:
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                heapq.heappush(
                    frontier,
                    (new_cost, counter, neighbor, path + [neighbor])
                )
                counter += 1

    return None, float("inf"), visit_order


def bfs_weighted_topology(start, goal):
    """BFS ignores weights and minimizes the number of edges."""
    queue = deque([(start, [start])])
    seen = {start}
    visit_order = []

    while queue:
        node, path = queue.popleft()
        visit_order.append(node)

        if node == goal:
            return path, visit_order

        for neighbor, _ in weighted_graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, visit_order


def calculate_path_cost(path):
    """Independently sum the weights of the edges in a returned path."""
    if not path:
        return None

    total = 0

    for current, next_node in zip(path, path[1:]):
        for neighbor, edge_cost in weighted_graph[current]:
            if neighbor == next_node:
                total += edge_cost
                break
        else:
            raise ValueError(
                f"Edge {current} -> {next_node} does not exist."
            )

    return total


if __name__ == "__main__":
    print("=== Weighted Graph ===")

    for node, edges in weighted_graph.items():
        print(f"{node}: {edges}")

    print("\n=== Uniform-Cost Search (UCS) ===")
    ucs_path, ucs_cost, ucs_order = ucs("A", "G")

    print("Processing order:", " -> ".join(ucs_order))
    print("Path:", " -> ".join(ucs_path) if ucs_path else "No path found")
    print("UCS reported cost:", ucs_cost)
    print("Independently calculated cost:", calculate_path_cost(ucs_path))

    print("\n=== BFS on the Same Weighted Topology ===")
    bfs_path, bfs_order = bfs_weighted_topology("A", "G")

    print("Processing order:", " -> ".join(bfs_order))
    print("Path:", " -> ".join(bfs_path) if bfs_path else "No path found")
    print("BFS path cost:", calculate_path_cost(bfs_path))
    print("Number of edges:", len(bfs_path) - 1 if bfs_path else 0)
