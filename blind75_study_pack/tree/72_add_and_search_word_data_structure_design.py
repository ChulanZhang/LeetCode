from typing import List, Optional, Dict, Set

# Add and Search Word (添加与搜索单词 - 数据结构设计) - Medium
# 🔑 核心考点: 前缀树 (Trie) + 带有通配符的递归 DFS 回溯
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：这道题是前缀树的进阶变体。我们需要设计一个单词查找系统，其中查找支持通配符 `'.'`（可以匹配任何单个字母）。如果不使用前缀树，随着添加单词的增加，大文本查询速度会严重变慢。使用前缀树后，我们可以利用 DFS 对通配符进行多路回溯查找。
#   - 思维推导: 
#     1. 节点设计与常规 Trie 一致：包含字典 `children` 和布尔值 `is_word`。
#     2. `addWord(word)`：常规前缀树插入操作，耗时 $O(L)$。
#     3. `search(word)`：需要处理通配符 `'.'`。我们设计一个递归的 DFS 匹配函数 `dfs(node, i)`，表示当前在 Trie 的 `node` 节点，去尝试匹配单词 `word` 从第 `i` 个索引开始的子串：
#        - 如果 `i == len(word)`，返回当前节点的 `is_word` 标记。
#        - 取出当前要匹配的字符 `char = word[i]`：
#          - **通配符处理**：如果 `char == '.'`，说明它可以代表任何子字符。我们必须遍历当前节点 `node.children` 中的**所有子节点**进行分支尝试：只要其中任何一个子分支调用 `dfs(child, i + 1)` 返回 `True`，当前搜索就判定成功，返回 `True`。如果全部子分支都失败，返回 `False`。
#          - **普通字符处理**：如果 `char` 在 `node.children` 中，递归进入下一层：`dfs(node.children[char], i + 1)`。否则，直接返回 `False`。

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """添加单词
        时间复杂度: O(L)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        """检索单词（支持通配符 '.'）
        时间复杂度: 最坏为 O(M) - M 为字典中字符总数（通配符较多时深度搜索），通常为 O(L)
        """
        def dfs(node, i):
            if i == len(word):
                return node.is_word
                
            char = word[i]
            if char == '.':
                # 通配符匹配：尝试遍历所有的子树分支
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # 常规字符匹配
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
                
        return dfs(self.root, 0)

