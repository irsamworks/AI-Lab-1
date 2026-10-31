# Lab 4: Informed Search — Heuristics and A*

## Objective

Implement A* search using a heuristic function and compare its performance with Uniform-Cost Search (UCS). Investigate how an overestimating heuristic can affect optimality.

## Files

* `lab4_astar_audit.py` — Python implementation of A* and UCS, including the overestimate experiment.
* `outputs/astar_ucs_output.txt` — Captured output comparing A* and UCS.
* `outputs/overestimate_output.txt` — Captured output from the overestimate experiment.

## Requirements

* Python 3
* No external libraries are required. The implementation uses Python's built-in `heapq` module.

## How to Run

Open a terminal in the `Lab-4` folder and run:

```powershell
python .\lab4_astar_audit.py
```

To capture the output:

```powershell
python .\lab4_astar_audit.py | Tee-Object .\outputs\astar_ucs_output.txt
```

## Graph

* S → A: 1
* S → B: 4
* A → C: 2
* B → G: 5
* C → G: 3

Start node: `S`
Goal node: `G`

## Heuristic

* h(S) = 5
* h(A) = 4
* h(B) = 4
* h(C) = 2
* h(G) = 0

## Expected Findings

With the supplied heuristic, A* returns `S → A → C → G` with cost 6. UCS returns the same optimal path with cost 6. In this run, A* expands 3 nodes and UCS expands 4 nodes.

In the overestimate experiment, h(C) is changed from 2 to 10. A* returns `S → B → G` with cost 9, although the optimal path still costs 6. This demonstrates that an overestimating heuristic can compromise the optimality guarantee.

## Counting Convention

A node is counted as expanded when its successors are examined. The goal node is recorded as processed but is not counted as expanded. Outdated priority-queue entries are ignored.
