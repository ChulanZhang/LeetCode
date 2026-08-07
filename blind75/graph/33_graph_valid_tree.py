from typing import List, Optional, Dict, Set

# LeetCode 261: Graph Valid Tree - Medium
# 🔗 Link: https://leetcode.com/problems/graph-valid-tree/
# 🔑 Key Points: Undirected Graph - Cycle Detection & Connectivity / Union-Find
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     An undirected graph is a tree if and only if it is **connected and acyclic**. In graph theory, a graph with `n` nodes is a tree if: 1. It has exactly `n - 1` edges. 2. It contains no cycles.
#   - Mathematical Derivation: 
#     We can use Union-Find (Disjoint Set) to check this efficiently:
#     1. If `len(edges) != n - 1`, the graph cannot be a tree, return False.
#     2. Initialize a disjoint set. Iterate through each edge `(u, v)` and try to union their sets:
#        - If `find(u) == find(v)` before union, `u` and `v` are already connected, so adding this edge creates a cycle. Return False.
#        - Otherwise, union their sets.
#     3. Since we have verified `edges == n - 1` and confirmed no cycles, the graph is guaranteed to be fully connected. Return True.

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time Complexity: O(N * alpha(N)) - alpha is the inverse Ackermann function, roughly O(1)
        # Space Complexity: O(N) - Disjoint Set parent array
        
        # Necessary condition: tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        parent = [i for i in range(n)]
        
        def find(i):
            if parent[i] == i:
                return i
            # Path compression optimization
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            # If roots are same, a cycle is detected
            if root_i == root_j:
                return False
            parent[root_i] = root_j
            return True
            
        for u, v in edges:
            if not union(u, v):
                return False  # Cycle detected
                
        return True

