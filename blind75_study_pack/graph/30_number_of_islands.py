from typing import List, Optional, Dict, Set

# Number of Islands (岛屿数量) - Medium
# 🔑 核心考点: 网格遍历 - 深度优先搜索 (DFS) / 广度优先搜索 (BFS) / 并查集 (Union Find)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要寻找被 '0'（水）包围的 '1'（陆地）组成的连通块的数量。这可以通过遍历网格来完成。当我们遇到一个 '1' 时，就代表找到了一个新岛屿，此时我们需要把与这个陆地相连的所有陆地都标记为已访问，避免重复计数。
#   - 思维推导: 
#     1. 遍历二维网格的每一个格子 `(r, c)`。
#     2. 如果 `grid[r][c] == '1'`：
#        - 岛屿计数器加 1。
#        - 启动 DFS 搜索：从当前格子出发，向上下左右四个方向扩散。一旦遇到相邻的 `'1'`，将其修改为 `'0'`（原地标记为已访问，这是一种常见的空间优化手段，避免使用 `visited` 集合）。
#        - DFS 扩散结束后，与该陆地连通的所有陆地都被沉没成了 `'0'`。
#     3. 继续遍历网格，后续遇到的 `'1'` 一定是新的独立岛屿。

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        时间复杂度: O(m * n) - 每个格子最多被访问常数次
        空间复杂度: O(m * n) - 最坏情况下（网格全为陆地）DFS 的递归调用栈深度
        """
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # 越界检查或遇到水 '0' 则停止扩散
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            # 原地淹没陆地，防止重复访问
            grid[r][c] = '0'
            # 递归向四周扩散
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    # 发现新岛屿，启动 DFS 将其全部连通区域标记为水
                    island_count += 1
                    dfs(r, c)
                    
        return island_count

