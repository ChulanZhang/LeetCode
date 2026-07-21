from typing import List, Optional, Dict, Set

# LeetCode 323: Number of Connected Components in an Undirected Graph - Medium
# 🔗 Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# 🔑 Key Points: Connected Components / Union-Find
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Given an undirected graph, we need to find the number of disconnected subgraphs. While DFS/BFS traversal works, Union-Find provides a highly concise and efficient disjoint set union solution.
#   - Mathematical Derivation: 
#     1. Initially, assume all `n` nodes are isolated components (`count = n`).
#     2. Iterate through each edge `(u, v)`:
#        - Find the roots of `u` and `v` in the disjoint set.
#        - If the roots are different, they belong to different components. We merge (union) the sets and decrement `count` by 1.
#        - If they have the same root, they are already connected, so we do nothing.
#     3. The final value of `count` is the number of connected components.

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time Complexity: O(N + E * alpha(N)) - N nodes, E edges. Virtually O(N + E)
        # Space Complexity: O(N) - Disjoint Set parent array
        parent = [i for i in range(n)]
        count = n
        
        def find(i):
            if parent[i] == i:
                return i
            # Path compression
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            nonlocal count
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Merge the components
                parent[root_i] = root_j
                # Decrement component count upon successful merge
                count -= 1
                
        for u, v in edges:
            union(u, v)
            
        return count

