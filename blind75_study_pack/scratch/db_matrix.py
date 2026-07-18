# Matrix category data
PROBLEMS = {
    "46_set_matrix_zeroes.py": {
        "title": "Set Matrix Zeroes (矩阵置零)",
        "difficulty": "Medium",
        "key_points": "矩阵标记 / 空间压缩 O(1) 优化",
        "analysis_intuition": "直觉：我们需要将所有包含 0 的行和列全部置零。如果直接在遍历中原地修改为 0，会干扰后面尚未遍历元素的判断，导致整张表都变成 0。如果声明另外的行、列数组来记录哪些行和列应该被置零，需要 $O(M + N)$ 的额外空间。如何优化至 $O(1)$？",
        "analysis_derivation": "利用矩阵的**第一行和第一列**来作为状态记录器：\n1. 记录第一行和第一列原本是否包含 0，分别存储在布尔变量 `first_row_zero` 和 `first_col_zero` 中。\n2. 遍历除第一行/第一列之外的整个矩阵，如果 `matrix[r][c] == 0`，就在它对应头部的第一行和第一列中做标记：令 `matrix[r][0] = 0` 和 `matrix[0][c] = 0`。\n3. 再次遍历这部分区间，如果某个位置所在的行首 `matrix[r][0] == 0` 或列首 `matrix[0][c] == 0`，就将该点置零：`matrix[r][c] = 0`。\n4. 最后根据初始的布尔变量，决定是否把第一行和第一列全部置零。\n这样我们就不必开辟任何新的空间，直接借用已有的首行首列内存搞定，空间复杂度为常数级 $O(1)$。",
        "code": """from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \"\"\"
        Do not return anything, modify matrix in-place instead.
        时间复杂度: O(M * N) - 需要遍历两遍矩阵
        空间复杂度: O(1) - 原地在首行首列作标记，无额外存储
        \"\"\"
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
"""
    },
    "47_spiral_matrix.py": {
        "title": "Spiral Matrix (螺旋矩阵)",
        "difficulty": "Medium",
        "key_points": "矩阵遍历边界模拟",
        "analysis_intuition": "直觉：我们需要以螺旋状（顺时针）遍历矩阵。这是一个模拟过程，我们可以通过在运动时动态维护网格当前的四个边界（上、下、左、右）来控制遍历的方向和终止条件。",
        "analysis_derivation": "1. 初始化四个边界：`top = 0`，`bottom = m - 1`，`left = 0`，`right = n - 1`。\n2. 当四个边界没有交叠（即 `left <= right` 且 `top <= bottom`）时循环执行：\n   - **向右走**：沿着 `top` 行从 `left` 到 `right`，遍历完后 `top += 1`。\n   - **向下走**：沿着 `right` 列从 `top` 到 `bottom`，遍历完后 `right -= 1`。\n   - **向左走**（注意此时需要再次验证 `top <= bottom`，防止单行重复打印）：沿着 `bottom` 行从 `right` 到 `left` 逆向，遍历后 `bottom -= 1`。\n   - **向上走**（同样需要再次验证 `left <= right`，防止单列重复打印）：沿着 `left` 列从 `bottom` 到 `top` 逆向，遍历后 `left += 1`。\n3. 当循环条件不满足时，我们就正好走完了矩阵内的所有元素。",
        "code": """from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        \"\"\"
        时间复杂度: O(M * N) - 刚好访问每个元素一次
        空间复杂度: O(1) - 仅使用用于辅助的几个边界指针
        \"\"\"
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
"""
    },
    "48_rotate_image.py": {
        "title": "Rotate Image (旋转图像)",
        "difficulty": "Medium",
        "key_points": "原地矩阵转置 + 行逆序",
        "analysis_intuition": "直觉：将矩阵顺时针旋转 90 度，如果声明一个同样大小的二维矩阵做过渡，可以用一行关系式 `new_matrix[j][n-1-i] = matrix[i][j]` 轻松做出来。但面试官会要求**原地 (In-place)** 修改，限制额外空间为 $O(1)$。",
        "analysis_derivation": "利用矩阵转置和对称性破局：\n如果仔细观察旋转的性质，我们会发现顺时针旋转 90 度实际上可以拆解为两步简单的基本几何操作：\n1. **矩阵转置**：沿着主对角线把对称的元素两两对调（即交换 `matrix[i][j]` 与 `matrix[j][i]`，保证 `j > i` 避免换回来）。此时，原来的行变成了列，但方向不对（逆了）。\n2. **水平翻转/行逆序**：对于转置后的矩阵，我们把每一行数组从中间一分为二，左右镜像对称翻转。也就是把每一行逆序一遍（即对每行执行 `matrix[i].reverse()`）。\n经过这两步，矩阵刚好就被完全顺时针旋转了 90 度，且所有调换都是原地双指针交换，不需要开辟任何外部存储，空间复杂度为常数级 $O(1)$。",
        "code": """from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        \"\"\"
        Do not return anything, modify matrix in-place instead.
        时间复杂度: O(N^2) - N 为矩阵的边长，转置和反转操作各自需要 O(N^2)
        空间复杂度: O(1) - 原地交换
        \"\"\"
        n = len(matrix)
        
        # 1. 矩阵转置：交换 matrix[i][j] 与 matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. 行逆序：反转每一行
        for i in range(n):
            matrix[i].reverse()
"""
    },
    "49_word_search.py": {
        "title": "Word Search (单词搜索)",
        "difficulty": "Medium",
        "key_points": "回溯算法 (Backtracking) / 深度优先搜索 (DFS)",
        "analysis_intuition": "直觉：我们需要在网格中寻找一条能拼写成单词的路径。由于不能重复使用相同的单元格，这是一个典型的图路径搜索问题。我们应当逐个格子检查，一旦第一个字母匹配成功，就启动 DFS 向其四周扩散搜索接下来的字母。",
        "analysis_derivation": "1. 遍历矩阵的每一个位置 `(r, c)`。若该处的字符与 `word` 的首字母相同，则以此作为起点，调用回溯函数 `dfs(r, c, 0)`（其中 `0` 代表当前要匹配的单词字符索引）。\n2. 回溯函数 `dfs(r, c, index)` 的逻辑：\n   - **基准情况**：如果 `index == len(word)`，说明单词已经全部匹配完毕，返回 `True`。\n   - **越界或不匹配**：如果 `r` 和 `c` 超出边界，或者当前格子已被访问过，或者 `grid[r][c] != word[index]`，说明此路不通，返回 `False`。\n   - **标记访问**：在继续递归之前，我们需要将当前位置标记为“已访问”。为了节省空间，我们原地修改当前元素为特殊符号（如 `'#'`），并在递归结束时撤销修改（回溯恢复现场：`grid[r][c] = word[index]`）。\n   - **四向递归**：向上下左右四个方向尝试继续匹配下一个字符：`index + 1`。只要有一个方向成功，就返回 `True`。\n3. 如果四向探索都失败，当前起点无效，回溯恢复，并尝试下一个网格起点。",
        "code": """from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        \"\"\"
        时间复杂度: O(M * N * 3^L) - M, N 为网格大小，L 为单词长度。对于每个起点，DFS 最多有 4 个方向，但除去来的方向，实际上分支因子是 3
        空间复杂度: O(L) - DFS 的最大系统递归调用栈深度为单词长度 L
        \"\"\"
        m, n = len(board), len(board[0])
        
        def dfs(r, c, index):
            # 匹配成功
            if index == len(word):
                return True
                
            # 边界及不匹配检查
            if (r < 0 or r >= m or c < 0 or c >= n or 
                board[r][c] != word[index]):
                return False
                
            # 暂存当前字符，标记为已访问，防止在同一次路径中被重复使用
            temp = board[r][c]
            board[r][c] = '#'
            
            # 向四个方向进行深度优先搜索
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
                     
            # 恢复现场（回溯的关键）
            board[r][c] = temp
            
            return found
            
        for r in range(m):
            for c in range(n):
                # 从与单词首字母相匹配的位置启动搜索
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False
"""
    }
}
