"""Extra edge-case checks for Lab 3.
Run from Lab-3: python lab3_edge_cases.py
"""
from collections import deque
import heapq

def bfs(graph, start, goal):
    q=deque([(start,[start])]); seen={start}; order=[]
    while q:
        node,path=q.popleft(); order.append(node)
        if node==goal: return path,order
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                seen.add(nxt); q.append((nxt,path+[nxt]))
    return None,order

def dfs(graph, start, goal):
    stack=[(start,[start])]; seen=set(); order=[]
    while stack:
        node,path=stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node)
        if node==goal: return path,order
        for nxt in reversed(graph.get(node,[])):
            if nxt not in seen: stack.append((nxt,path+[nxt]))
    return None,order

def dls(graph,start,goal,limit):
    order=[]
    def visit(node,path,depth):
        order.append(node)
        if node==goal: return "FOUND",path
        if depth==limit:
            return ("CUTOFF",None) if any(n not in path for n in graph.get(node,[])) else ("FAILURE",None)
        cutoff=False
        for nxt in graph.get(node,[]):
            if nxt in path: continue
            status,p=visit(nxt,path+[nxt],depth+1)
            if status=="FOUND": return status,p
            if status=="CUTOFF": cutoff=True
        return ("CUTOFF",None) if cutoff else ("FAILURE",None)
    status,path=visit(start,[start],0)
    return status,path,order

def ucs(graph,start,goal):
    heap=[(0,0,start,[start])]; serial=1; best={start:0}; order=[]
    while heap:
        cost,_,node,path=heapq.heappop(heap)
        if cost>best.get(node,float("inf")): continue
        order.append(node)
        if node==goal: return path,cost,order
        for nxt,w in graph.get(node,[]):
            nc=cost+w
            if nc<best.get(nxt,float("inf")):
                best[nxt]=nc; heapq.heappush(heap,(nc,serial,nxt,path+[nxt])); serial+=1
    return None,float("inf"),order

def run_case(label, graph, start, goal, limit=3):
    print(f"\n--- {label} ---")
    p,o=bfs(graph,start,goal); print("BFS:", " -> ".join(p) if p else "No path", "| order:", " -> ".join(o))
    p,o=dfs(graph,start,goal); print("DFS:", " -> ".join(p) if p else "No path", "| order:", " -> ".join(o))
    s,p,o=dls(graph,start,goal,limit); print(f"DLS (limit={limit}):",s,"| path:"," -> ".join(p) if p else "None","| order:"," -> ".join(o))
    wg={n:[(child,1) for child in children] for n,children in graph.items()}
    p,c,o=ucs(wg,start,goal); print("UCS:"," -> ".join(p) if p else "No path","| cost:",c,"| order:"," -> ".join(o))

if __name__=="__main__":
    run_case("Start equals goal", {"A":["B"],"B":[]}, "A", "A", 2)
    run_case("Unreachable goal", {"A":["B"],"B":[],"Z":[]}, "A", "Z", 3)
    run_case("Graph containing a cycle", {"A":["B"],"B":["C"],"C":["A","G"],"G":[]}, "A", "G", 3)
