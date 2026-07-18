from typing import List, Optional, Dict, Set

# Pacific Atlantic Water Flow (太平洋大西洋水流问题) - Medium
# 🔑 核心考点: 多源深度优先搜索 (DFS) / 逆向遍历
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们要找出哪些格子既能流向太平洋（网格左侧和上方），又能流向大西洋（网格右侧和下方）。如果对每个格子分别运行一遍搜索，时间复杂度将是 O((M * N)^2)，会超时。
#   - 思维推导: 
#     逆向思维破局：
#     与其从网格的每个点“向下流”寻找海洋，不如**从太平洋和大西洋的边界“向上爬”**（逆水流方向移动，水流是从高往低，所以逆向就是从低往高，只能走到高度大于或等于当前格子的相邻格）。
#     1. 我们声明两个布尔矩阵 `pacific_reach` 和 `atlantic_reach`，记录从对应的洋边界出发可以逆向到达的所有网格位置。
#     2. 从太平洋的边界（第一行和第一列）出发运行 DFS，标记所有可达的位置。
#     3. 从大西洋的边界（最后一行和最后一列）出发运行 DFS，标记所有可达的位置。
#     4. 遍历整个网格，若某个格子在两个布尔矩阵中均为 `True`，说明它既能流向太平洋也能流向大西洋，加入结果集。时间复杂度大幅降低为 O(M * N)。

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        时间复杂度: O(m * n) - 每个格子最多被 DFS 访问常数次
        空间复杂度: O(m * n) - 存储可达状态矩阵与调用栈
        """
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reach = [[False] * n for _ in range(m)]
        atlantic_reach = [[False] * n for _ in range(m)]
        
        def dfs(r, c, reach, prev_height):
            # 边界检查、是否访问过、以及是否满足逆水流方向（新高度必须大于或等于旧高度）
            if (r < 0 or r >= m or c < 0 or c >= n or 
                reach[r][c] or heights[r][c] < prev_height):
                return
            reach[r][c] = True
            
            # 向四个方向扩散
            dfs(r + 1, c, reach, heights[r][c])
            dfs(r - 1, c, reach, heights[r][c])
            dfs(r, c + 1, reach, heights[r][c])
            dfs(r, c - 1, reach, heights[r][c])
            
        # 从太平洋（第一行/第一列）和大西洋（最后一行/最后一列）的边界出发进行逆向 DFS
        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, n - 1, atlantic_reach, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(m - 1, j, atlantic_reach, heights[m - 1][j])
            
        # 筛选出既能到达太平洋也能到达大西洋的网格坐标
        res = []
        for r in range(m):
            for c in range(n):
                if pacific_reach[r][c] and atlantic_reach[r][c]:
                    res.append([r, c])
        return res

