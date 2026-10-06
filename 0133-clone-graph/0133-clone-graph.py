"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(curr):
            # if already cloned
            if curr in visited:
                return visited[curr]
            else:
                # create a copy of the curr node
                clone = Node(curr.val)
                visited[curr] = clone

                for neighbor in curr.neighbors:
                    clone.neighbors.append(dfs(neighbor))
                
                return clone

        return dfs(node)

# TC: O(N + M) for nodes and edges
# SC: O(N + M) for nodes and edges