from typing import List, Optional, Dict, Set

# Set Matrix Zeroes (矩阵置零) - Medium
# 🔑 核心考点: 矩阵标记 / 空间压缩 O(1) 优化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要将所有包含 0 的行和列全部置零。如果直接在遍历中原地修改为 0，会干扰后面尚未遍历元素的判断，导致整张表都变成 0。如果声明另外的行、列数组来记录哪些行和列应该被置零，需要 $O(M + N)$ 的额外空间。如何优化至 $O(1)$？
#   - 思维推导: 
#     利用矩阵的**第一行和第一列**来作为状态记录器：
#     1. 记录第一行和第一列原本是否包含 0，分别存储在布尔变量 `first_row_zero` 和 `first_col_zero` 中。
#     2. 遍历除第一行/第一列之外的整个矩阵，如果 `matrix[r][c] == 0`，就在它对应头部的第一行和第一列中做标记：令 `matrix[r][0] = 0` 和 `matrix[0][c] = 0`。
#     3. 再次遍历这部分区间，如果某个位置所在的行首 `matrix[r][0] == 0` 或列首 `matrix[0][c] == 0`，就将该点置零：`matrix[r][c] = 0`。
#     4. 最后根据初始的布尔变量，决定是否把第一行和第一列全部置零。
#     这样我们就不必开辟任何新的空间，直接借用已有的首行首列内存搞定，空间复杂度为常数级 $O(1)$。

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        时间复杂度: O(M * N) - 需要遍历两遍矩阵
        空间复杂度: O(1) - 原地在首行首列作标记，无额外存储
        """
        if not matrix:
            return
            
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # 1. 检测第一行和第一列自己是否原本含有 0
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_zero = True
                break
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True
                break
                
        # 2. 遍历其余元素，把行列的 0 标记投影到第一行和第一列上
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # 3. 根据第一行第一列的投影标记，将对应的内层元素置零
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # 4. 最后单独处理第一行和第一列自己
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0

