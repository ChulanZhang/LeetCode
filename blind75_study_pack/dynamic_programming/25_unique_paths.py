from typing import List, Optional, Dict, Set

# Unique Paths (不同路径) - Medium
# 🔑 核心考点: 网格动态规划 / 空间压缩
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：机器人要走到位置 `(i, j)`，因为它只能向下或向右移动，所以它只能从它的上方格 `(i-1, j)` 或者它的左侧格 `(i, j-1)` 走过来。因此，走到 `(i, j)` 的路径数就是两者之和。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i][j]` 为走到网格 `(i, j)` 的唯一路径数。
#     状态转移方程：
#     `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
#     第一行和第一列都初始化为 1，因为只能一直向右或一直向下走。
#     空间优化：由于计算当前行的状态只依赖于当前行的左侧状态和上一行的正上方状态，我们可以只维护一维数组（长度为网格宽度 `n`），不断用 `row[j] = row[j] + row[j-1]`（左侧加上正上方）来更新它，空间复杂度可以降低到 O(n)。

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        时间复杂度: O(m * n) - 填充整个网格
        空间复杂度: O(n) - 维护一行状态
        """
        # 初始第一行路径数均为 1
        row = [1] * n
        
        # 逐行更新
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(1, n):
                # new_row[j] = 上方格的值 (new_row[j]) + 左侧格的值 (new_row[j-1])
                # 注意在行滚动中，row[j] 存的就是上一行正上方格的值
                new_row[j] = row[j] + new_row[j-1]
            row = new_row
            
        return row[n-1]

