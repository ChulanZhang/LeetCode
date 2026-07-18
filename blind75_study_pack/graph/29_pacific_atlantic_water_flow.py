from typing import List, Optional, Dict, Set

# Pacific Atlantic Water Flow - Medium
# 🔑 Key Points: Multi-Source DFS / Reverse Search
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to find grid coordinates that can flow to both the Pacific Ocean (top/left) and the Atlantic Ocean (bottom/right). Running a separate flow search from every cell would take O((M * N)^2) time, which is too slow.
#   - Mathematical Derivation: 
#     Reverse thinking: Instead of starting from each grid cell and searching downwards to the oceans, we start from the ocean boundaries and search backwards (climbing up to adjacent cells with height >= current height).
#     1. Declare two boolean matrices: `pacific_reach` and `atlantic_reach` to store reachable coordinates from the respective ocean.
#     2. Run DFS from the Pacific boundaries (first row and first column) to mark all reachable cells.
#     3. Run DFS from the Atlantic boundaries (last row and last column) to mark all reachable cells.
#     4. Traverse the grid. Any cell marked True in both matrices can flow to both oceans. This reduces the time complexity to O(M * N).

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(m * n) - Each cell is visited a constant number of times
        # Space Complexity: O(m * n) - Reachability grids and recursive DFS stack
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reach = [[False] * n for _ in range(m)]
        atlantic_reach = [[False] * n for _ in range(m)]
        
        def dfs(r, c, reach, prev_height):
            # Base cases: out of bounds, already visited, or water cannot flow backwards (height < prev_height)
            if (r < 0 or r >= m or c < 0 or c >= n or 
                reach[r][c] or heights[r][c] < prev_height):
                return
            reach[r][c] = True
            
            # Explore 4 directions
            dfs(r + 1, c, reach, heights[r][c])
            dfs(r - 1, c, reach, heights[r][c])
            dfs(r, c + 1, reach, heights[r][c])
            dfs(r, c - 1, reach, heights[r][c])
            
        # Run DFS from the Pacific and Atlantic boundaries
        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, n - 1, atlantic_reach, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(m - 1, j, atlantic_reach, heights[m - 1][j])
            
        # Find intersections of Pacific and Atlantic reachability
        res = []
        for r in range(m):
            for c in range(n):
                if pacific_reach[r][c] and atlantic_reach[r][c]:
                    res.append([r, c])
        return res

