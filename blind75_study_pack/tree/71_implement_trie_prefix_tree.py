from typing import List, Optional, Dict, Set

# Implement Trie (Prefix Tree) - Medium
# 🔑 Key Points: Trie Structure / Nested Dictionaries
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A Trie (Prefix Tree) is a tree structure used for fast string retrieval and autocomplete queries. Each node in the Trie represents a character. A path from the root to a node spells out a word.
#   - Mathematical Derivation: 
#     Trie Node Structure Design:
#     We can implement a Trie node using a dictionary `children` mapping characters to child `TrieNode` objects, and a boolean flag `is_word` indicating if the node marks the end of a complete word.
#     1. `insert(word)`: Iterate through the word's characters. If a character is not in the current node's `children`, insert a new `TrieNode`. Move the pointer to the child node. At the end of the word, set `is_word = True`.
#     2. `search(word)`: Traverse the Trie following the word's characters. If a character is missing, return False. At the end, return `is_word` (which must be True for the word to exist).
#     3. `startsWith(prefix)`: Traverse the Trie following the prefix. If the traversal succeeds, the prefix exists. Return True.

class TrieNode:
    def __init__(self):
        # Map of children nodes {char: TrieNode}
        self.children = {}
        # Boolean to check if node marks the end of a word
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Time Complexity: O(L) - L is word length
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Time Complexity: O(L)
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        # Time Complexity: O(L)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

