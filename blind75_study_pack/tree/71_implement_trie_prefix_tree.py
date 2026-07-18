from typing import List, Optional, Dict, Set

# Implement Trie (Prefix Tree) (实现 Trie (前缀树)) - Medium
# 🔑 核心考点: 前缀树设计 / 嵌套哈希结构
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：Trie 树（前缀树）是一种哈希树变体，常用于快速检索字符串前缀或进行自动补全。Trie 树的每个节点代表一个字符。根节点不包含字符，除根节点外每一个节点都仅包含一个字符；从根节点到某一个节点，路径上经过的字符连接起来就是该节点对应的字符串。
#   - 思维推导: 
#     Trie 节点结构设计：
#     我们可以将每个节点定义为一个字典 `children`，键（Key）为子字符，值（Value）为指向下一个 Trie 节点实例的指针。同时，使用一个布尔变量 `is_word` 记录当前节点是否是一个单词的结束标记。
#     1. `insert(word)`：从根节点出发，遍历单词的每个字符 `char`。如果 `char` 不在当前节点的 `children` 字典中，就创建一个新的 Trie 节点加入其中。然后指针移动到该子节点。遍历完后，将最后一个节点的 `is_word` 设为 `True`。
#     2. `search(word)`：沿着 `children` 指针向下检索单词的每一个字符，如果中途断掉则说明该单词不存在，返回 `False`；如果顺利到达结尾，返回最后一个节点的 `is_word` 状态。
#     3. `startsWith(prefix)`：执行与 `search` 相同的检索过程。如果顺利走完前缀的所有字符，说明前缀存在（无需关注最后一个节点是否是单词结尾），返回 `True`；中途断掉则返回 `False`。

class TrieNode:
    def __init__(self):
        # 存储子节点映射 {字符: TrieNode}
        self.children = {}
        # 标记当前节点是否是单词的尾字符
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """插入一个单词
        时间复杂度: O(L) - L 为单词长度
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        """查询单词是否存在
        时间复杂度: O(L)
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        """查询是否存在以该前缀开头的单词
        时间复杂度: O(L)
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

