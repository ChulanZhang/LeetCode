from typing import List, Optional, Dict, Set

# Spiral Matrix (螺旋矩阵) - Medium
# 🔑 核心考点: 矩阵遍历边界模拟
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要以螺旋状（顺时针）遍历矩阵。这是一个模拟过程，我们可以通过在运动时动态维护网格当前的四个边界（上、下、左、右）来控制遍历的方向和终止条件。
#   - 思维推导: 
#     1. 初始化四个边界：`top = 0`，`bottom = m - 1`，`left = 0`，`right = n - 1`。
#     2. 当四个边界没有交叠（即 `left <= right` 且 `top <= bottom`）时循环执行：
#        - **向右走**：沿着 `top` 行从 `left` 到 `right`，遍历完后 `top += 1`。
#        - **向下走**：沿着 `right` 列从 `top` 到 `bottom`，遍历完后 `right -= 1`。
#        - **向左走**（注意此时需要再次验证 `top <= bottom`，防止单行重复打印）：沿着 `bottom` 行从 `right` 到 `left` 逆向，遍历后 `bottom -= 1`。
#        - **向上走**（同样需要再次验证 `left <= right`，防止单列重复打印）：沿着 `left` 列从 `bottom` 到 `top` 逆向，遍历后 `left += 1`。
#     3. 当循环条件不满足时，我们就正好走完了矩阵内的所有元素。

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        时间复杂度: O(M * N) - 刚好访问每个元素一次
        空间复杂度: O(1) - 仅使用用于辅助的几个边界指针
        """
        if not matrix:
            return []
            
        m, n = len(matrix), len(matrix[0])
        res = []
        
        # 定义当前上下左右边界
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while left <= right and top <= bottom:
            # 1. 从左到右遍历上边界
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. 从上到下遍历右边界
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # 3. 从右到左遍历下边界
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
                
            if left <= right:
                # 4. 从下到上遍历左边界
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
                
        return res

