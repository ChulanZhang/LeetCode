from typing import List, Optional, Dict, Set

# Word Search (单词搜索) - Medium
# 🔑 核心考点: 回溯算法 (Backtracking) / 深度优先搜索 (DFS)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要在网格中寻找一条能拼写成单词的路径。由于不能重复使用相同的单元格，这是一个典型的图路径搜索问题。我们应当逐个格子检查，一旦第一个字母匹配成功，就启动 DFS 向其四周扩散搜索接下来的字母。
#   - 思维推导: 
#     1. 遍历矩阵的每一个位置 `(r, c)`。若该处的字符与 `word` 的首字母相同，则以此作为起点，调用回溯函数 `dfs(r, c, 0)`（其中 `0` 代表当前要匹配的单词字符索引）。
#     2. 回溯函数 `dfs(r, c, index)` 的逻辑：
#        - **基准情况**：如果 `index == len(word)`，说明单词已经全部匹配完毕，返回 `True`。
#        - **越界或不匹配**：如果 `r` 和 `c` 超出边界，或者当前格子已被访问过，或者 `grid[r][c] != word[index]`，说明此路不通，返回 `False`。
#        - **标记访问**：在继续递归之前，我们需要将当前位置标记为“已访问”。为了节省空间，我们原地修改当前元素为特殊符号（如 `'#'`），并在递归结束时撤销修改（回溯恢复现场：`grid[r][c] = word[index]`）。
#        - **四向递归**：向上下左右四个方向尝试继续匹配下一个字符：`index + 1`。只要有一个方向成功，就返回 `True`。
#     3. 如果四向探索都失败，当前起点无效，回溯恢复，并尝试下一个网格起点。

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        时间复杂度: O(M * N * 3^L) - M, N 为网格大小，L 为单词长度。对于每个起点，DFS 最多有 4 个方向，但除去来的方向，实际上分支因子是 3
        空间复杂度: O(L) - DFS 的最大系统递归调用栈深度为单词长度 L
        """
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

