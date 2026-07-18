from typing import List, Optional, Dict, Set

# Rotate Image (旋转图像) - Medium
# 🔑 核心考点: 原地矩阵转置 + 行逆序
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：将矩阵顺时针旋转 90 度，如果声明一个同样大小的二维矩阵做过渡，可以用一行关系式 `new_matrix[j][n-1-i] = matrix[i][j]` 轻松做出来。但面试官会要求**原地 (In-place)** 修改，限制额外空间为 $O(1)$。
#   - 思维推导: 
#     利用矩阵转置和对称性破局：
#     如果仔细观察旋转的性质，我们会发现顺时针旋转 90 度实际上可以拆解为两步简单的基本几何操作：
#     1. **矩阵转置**：沿着主对角线把对称的元素两两对调（即交换 `matrix[i][j]` 与 `matrix[j][i]`，保证 `j > i` 避免换回来）。此时，原来的行变成了列，但方向不对（逆了）。
#     2. **水平翻转/行逆序**：对于转置后的矩阵，我们把每一行数组从中间一分为二，左右镜像对称翻转。也就是把每一行逆序一遍（即对每行执行 `matrix[i].reverse()`）。
#     经过这两步，矩阵刚好就被完全顺时针旋转了 90 度，且所有调换都是原地双指针交换，不需要开辟任何外部存储，空间复杂度为常数级 $O(1)$。

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        时间复杂度: O(N^2) - N 为矩阵的边长，转置和反转操作各自需要 O(N^2)
        空间复杂度: O(1) - 原地交换
        """
        n = len(matrix)
        
        # 1. 矩阵转置：交换 matrix[i][j] 与 matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. 行逆序：反转每一行
        for i in range(n):
            matrix[i].reverse()

