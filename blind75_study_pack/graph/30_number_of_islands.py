from typing import List, Optional, Dict, Set

# LeetCode 200: Number of Islands - Medium
# 🔗 Link: https://leetcode.com/problems/number-of-islands/
# 🔑 Key Points: Grid Search - DFS / BFS / Union-Find
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to find the number of connected components of '1's (land) surrounded by '0's (water). When we encounter a '1', it marks the discovery of a new island. We must then run DFS/BFS to traverse and sink all connected lands to avoid double counting.
#   - Mathematical Derivation: 
#     1. Iterate through every cell `(r, c)` of the grid.
#     2. If `grid[r][c] == '1'`:
#        - Increment the island counter.
#        - Start DFS from `(r, c)`. For each adjacent land cell, we sink it by setting its value to `'0'` (in-place modification is a great space optimization that avoids a `visited` set).
#     3. Continue scanning the grid; any future `'1'` encountered must belong to a separate, new island.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(m * n) - Each grid cell is visited a constant number of times
        # Space Complexity: O(m * n) - Recursion stack in the worst case (all land)
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base cases: out of bounds or water cell
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            # Sink current land to prevent visiting it again
            grid[r][c] = '0'
            # Recursively explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    island_count += 1
                    # Initiate DFS to sink all connected parts of the island
                    dfs(r, c)
                    
        return island_count

