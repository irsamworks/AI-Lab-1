
from collections import deque

# Original graph from Section 3.2
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def bfs(start, goal):
    queue = deque([(start, [start])])
    seen = {start}
    visit_order = []

    while queue:
        node, path = queue.popleft()
        visit_order.append(node)

        # Stop when the goal is processed
        if node == goal:
            return path, visit_order

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, visit_order


def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    visit_order = []

    while stack:
        node, path = stack.pop()

        if node in seen:
            continue

        seen.add(node)
        visit_order.append(node)

        # Stop when the goal is processed
        if node == goal:
            return path, visit_order

        # Reverse insertion preserves left-to-right visit order
        for neighbor in reversed(graph[node]):
            if neighbor not in seen:
                stack.append((neighbor, path + [neighbor]))

    return None, visit_order


# Run BFS
bfs_path, bfs_order = bfs("A", "G")

print("=== Breadth-First Search (BFS) ===")
print("Visit order:", " -> ".join(bfs_order))
print("Final path:", " -> ".join(bfs_path) if bfs_path else "No path found")

# Run DFS
dfs_path, dfs_order = dfs("A", "G")

print("\n=== Depth-First Search (DFS) ===")
print("Visit order:", " -> ".join(dfs_order))
print("Final path:", " -> ".join(dfs_path) if dfs_path else "No path found")

