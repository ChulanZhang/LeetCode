from typing import List, Optional, Dict, Set

# Word Search II (单词搜索 Ⅱ) - Hard
# 🔑 核心考点: 前缀树 (Trie) + 二维网格回溯 (Backtracking DFS) + 剪枝优化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：本题是“单词搜索 I”的升级版。如果对于 `words` 列表中的每个单词都分别在网格里运行一遍回溯 DFS，时间复杂度是 O(W * M * N * 3^L)（W 是单词数量），会严重超时。我们需要一次性在网格中搜索所有的单词。
#   - 思维推导: 
#     前缀树加速网格回溯与剪枝破局：
#     与其对单词列表进行外层迭代，不如**将所有待检索的单词构建到一棵前缀树 (Trie) 中**，然后我们在网格的每个位置启动 DFS 搜索时，**让网格的移动与 Trie 树的指针移动同步进行**。
#     1. **建树**：将 `words` 写入 Trie 树。为了方便，我们在单词结尾的节点上直接保存该单词的值（如 `node.word = word`），这样一旦在搜索中匹配到单词节点，可以直接获取到完整的单词。
#     2. **网格 DFS**：在位置 `(r, c)`：
#        - 如果当前网格字符 `char` 在当前 Trie 节点 `node.children` 中，说明这是一条有潜力的匹配路径。我们移动到 `child_node = node.children[char]`。
#        - 检查 `child_node`：如果它包含 `word` 属性，说明我们找到了一个有效的单词，加入结果集中。**重要优化：立即将 `child_node.word` 设为 `None`，防止同一个单词在不同网格位置被重复搜出来加入结果集。**
#        - 原地标记当前格子已被访问（如 `board[r][c] = '#'`），然后向四周递归继续搜索。
#        - 回溯恢复现场（`board[r][c] = char`）。
#     3. **高阶剪枝优化**：当一个叶子节点的单词被找到后，或者一个节点的所有子树都为空时，说明这部分的 Trie 树枝已经没有利用价值了。我们可以在回溯时**就地将该无效子节点从父节点的 children 字典中删除**（剪枝）。这可以极大防止冗余的重复路径探索，是能通过力扣超强测试用例的关键。

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 存储匹配成功的完整单词

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        时间复杂度: O(M * N * 4 * 3^(L-1)) - M, N 为网格边长，L 为单词最大长度
        空间复杂度: O(W * L) - Trie 树占用的存储空间，W 为单词数，L 为最大长度
        """
        # 1. 构建前缀树
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
            
        m, n = len(board), len(board[0])
        res = []
        
        # 2. 网格回溯 DFS 函数
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]
            
            # 如果匹配成功一个单词，将其加入结果
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # 防止重复添加
                
            # 临时标记已访问
            board[r][c] = '#'
            
            # 探索四周邻居
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_char = board[nr][nc]
                    if next_char in curr_node.children:
                        dfs(nr, nc, curr_node)
                        
            # 回溯恢复现场
            board[r][c] = char
            
            # 高阶剪枝优化：如果当前节点没有子节点了，从父节点中删除它
            if not curr_node.children:
                parent_node.children.pop(char)
                
        # 3. 遍历网格每个格子作为起点尝试搜索
        for r in range(m):
            for c in range(n):
                start_char = board[r][c]
                if start_char in root.children:
                    dfs(r, c, root)
                    
        return res

