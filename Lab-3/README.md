# Lab 3: Uninformed Search Algorithms

**Course:** CAI601400 — Artificial Intelligence Lab
**Week:** 3
**Topics:** BFS, DFS, DLS, IDDFS, and UCS

## Objective

Implement and compare uninformed search algorithms on a graph representing an emergency-exit problem.

## Graph for BFS, DFS, DLS, and IDDFS

The original directed graph has A as the start node and G as the goal node.

* A → B, C
* B → D, E
* C → F
* E → G

The successor order is preserved from the lab manual.

## Files

* `lab3_bfs_dfs.py`: Breadth-First Search and Depth-First Search.
* `lab3_depth_search.py`: Depth-Limited Search and Iterative Deepening DFS.
* `lab3_ucs.py`: Uniform-Cost Search and BFS comparison on a weighted graph.
* `outputs/`: Captured program outputs.

## Requirements

Python 3. No external packages are required.

## Run the Programs

From the project root, run:

```powershell
python .\Lab-3\lab3_bfs_dfs.py
python .\Lab-3\lab3_depth_search.py
python .\Lab-3\lab3_ucs.py
```

## Weighted Graph

The weighted experiment retains the original edges and adds C → G as an alternative corridor.

| Edge  | Cost |
| ----- | ---: |
| A → B |    1 |
| A → C |    1 |
| B → D |    1 |
| B → E |    1 |
| C → F |    1 |
| E → G |    1 |
| C → G |   11 |

The original corridors have cost 1 each, and the added corridor C → G has cost 11. These are the explicitly selected weights for this experiment, consistent with the path costs specified in Section 3.7 of the lab manual.

## Key Results

* BFS path: A → B → E → G on the original graph.
* DFS path: A → B → E → G on the original graph.
* DLS finds G when the depth limit is at least 3.
* IDDFS finds G at depth 3.
* BFS on the weighted topology selects A → C → G, with cost 12.
* UCS selects A → B → E → G, with minimum cost 3.

## Assumptions and Limitations

The graph is directed. Successor order is fixed for reproducible traces. UCS assumes nonnegative edge costs. BFS minimizes edge count rather than weighted travel cost.

## Source Attribution

The original graph structure and task requirements are taken from the CAI601400 Artificial Intelligence Lab Manual, Sections 3.2 and 3.5–3.8. The Python implementations were written for this lab exercise.
