\# Lab 5: Adversarial Search — Minimax and Alpha-Beta Pruning



\*\*Course:\*\* CAI601400 — Artificial Intelligence

\*\*Week:\*\* 5

\*\*Lectures:\*\* L11–L12

\*\*CLO:\*\* CLO2 (C3: Apply)

\*\*Instructor:\*\* Rasikh Ali



\## Objective



Implement Minimax and Alpha-Beta Pruning for fixed-depth binary game trees, count evaluated terminal leaves, and compare the algorithms under different leaf orderings.



\## Files



\* `lab5\_minimax\_alphabeta.py` — Python implementation and experiments.

\* `outputs/lab5\_final\_output.txt` — Captured program output and traces.



\## Experiments



1\. Minimax and Alpha-Beta on the manual's supplied example.

2\. Reordered leaf values.

3\. Comparison of evaluated leaves on an eight-leaf tree.

4\. A second eight-leaf ordering.

5\. Edge-case test using a single terminal leaf.



\## Results



In the third and fourth experiments, Minimax evaluated 8 leaves while Alpha-Beta evaluated 6 leaves. Both algorithms returned root value 5, demonstrating that pruning reduced leaf evaluations without changing the Minimax result for these trees.



In the first two experiments, both algorithms evaluated 8 leaves. This shows that pruning efficiency depends on the tree values and branch ordering.



The single-terminal-leaf test returned value 7 in both algorithms, with one evaluated leaf each.



\## How to Run



From the `Lab-5` directory, execute:



```powershell

python .\\lab5\_minimax\_alphabeta.py

```



To save the output:



```powershell

python .\\lab5\_minimax\_alphabeta.py | Tee-Object .\\outputs\\lab5\_final\_output.txt

```



\## Reflection



Minimax selects a move by assuming both players choose actions optimally. Alpha-Beta Pruning uses alpha and beta bounds to skip branches that cannot improve the final decision. The experiments show that both algorithms can return the same root value while Alpha-Beta evaluates fewer leaves when the ordering allows effective pruning.



\## Limitation



The experiments use fixed-depth binary trees and numerical terminal utilities. They do not implement a complete playable game or a heuristic evaluation function for non-terminal states.



