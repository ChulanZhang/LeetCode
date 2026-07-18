from typing import List, Optional, Dict, Set

# Clone Graph - Medium
# 🔑 Key Points: Graph Traversals - DFS / BFS with Hash Map Mapping
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To clone a graph, we must traverse all of its nodes. However, because graphs can contain cycles, we must keep track of nodes we have already copied to prevent falling into infinite recursion.
#   - Mathematical Derivation: 
#     We use a hash map `cloned` to store the mapping from original nodes to their cloned counterparts (`old_node -> new_node`).
#     For each visited node:
#     1. If it is already in `cloned`, return the cloned node directly.
#     2. Otherwise, instantiate a new node with the same value and save it in `cloned`.
#     3. Recursively copy all its neighbors, adding each cloned neighbor to the new node's neighbor list.
#     This DFS + Hash Map pattern ensures every node and edge is copied once without cycles.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Time Complexity: O(V + E) - Each node and edge is visited once
        # Space Complexity: O(V) - Recursion stack and cloned hash map
        if not node:
            return None
            
        cloned = {}
        
        def dfs(curr):
            # If already cloned, return the cached clone to break cycles
            if curr in cloned:
                return cloned[curr]
                
            # Instantiate the copy and cache it immediately
            copy = Node(curr.val)
            cloned[curr] = copy
            
            # Recursively copy all neighbor nodes
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)

