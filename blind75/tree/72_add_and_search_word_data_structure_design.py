from typing import List, Optional, Dict, Set

# LeetCode 211: Add and Search Word - Medium
# 🔗 Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# 🔑 Key Points: Trie + Wildcard DFS Backtracking
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     This problem adds wildcard searches to the standard Trie, where `'.'` can match any single character. While adding words is identical to insertion in a Trie, searching requires a DFS-based backtracking approach to handle the `'.'` character.
#   - Mathematical Derivation: 
#     1. Node structure: Standard Trie node (`children` dict, `is_word` boolean).
#     2. `addWord(word)`: Standard Trie word insertion.
#     3. `search(word)`: Define a recursive helper `dfs(node, i)` that checks matching starting from character index `i` of `word` at Trie node `node`:
#        - If `i == len(word)`, return `node.is_word`.
#        - Let `char = word[i]`:
#          - **Wildcard dot**: If `char == '.'`, we must try all branches in `node.children.values()`. If any branch returns True for `dfs(child, i + 1)`, search is successful. Return True. If all fail, return False.
#          - **Standard character**: If `char` exists in `node.children`, recursively check the child: `dfs(node.children[char], i + 1)`. Otherwise, return False.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Time Complexity: O(L) - L is word length
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Time Complexity: O(M) worst case - M is total nodes in the Trie (wildcard search), usually O(L)
        def dfs(node, i):
            if i == len(word):
                return node.is_word
                
            char = word[i]
            if char == '.':
                # Wildcard search: try all possible child paths
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Direct character match
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
                
        return dfs(self.root, 0)

