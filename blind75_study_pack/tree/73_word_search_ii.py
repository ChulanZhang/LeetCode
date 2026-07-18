from typing import List, Optional, Dict, Set

# Word Search II - Hard
# 🔑 Key Points: Trie + Grid DFS Backtracking + Node Deletion Pruning
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     This is Word Search I with a list of words. Searching for each word individually takes O(W * M * N * 3^L) time (where W is word count), which will time out. We must search for all words in a single grid scan.
#   - Mathematical Derivation: 
#     Trie-Accelerated Grid DFS Backtracking:
#     Instead of looping through words, we **store all target words in a Trie**. During the grid DFS traversal, we synchronize the grid position shifts with navigation in the Trie.
#     1. **Trie building**: Insert all words into the Trie. For convenience, store the actual word string at its leaf node: `node.word = word`.
#     2. **Grid DFS**: At `(r, c)`:
#        - If `board[r][c] = char` is in the Trie node's children, move to `child_node = node.children[char]`.
#        - If `child_node` has a `word` attribute, we found a match. Add it to results and **immediately clear `child_node.word = None` to prevent duplicate matches**.
#        - Mark the grid cell as visited (`board[r][c] = '#'`), recursively call DFS in 4 directions, then restore the cell's character (backtrack).
#     3. **Trie Pruning Optimization**: If a node has no children (`not curr_node.children`), it is a dead end. We can delete it from its parent's `children` map on backtracking. This pruning prevents exploring redundant grid paths and is crucial to passing strict constraints.

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word if the node marks a word's end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time Complexity: O(M * N * 4 * 3^(L-1)) - M, N are board dimensions, L is maximum word length
        # Space Complexity: O(W * L) - Space to store words in the Trie
        
        # 1. Build the Trie
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
        
        # 2. Backtracking DFS
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]
            
            # Match found, record word and clear to prevent duplicate matches
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None
                
            # Temporarily mark grid cell as visited
            board[r][c] = '#'
            
            # Explore 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_char = board[nr][nc]
                    if next_char in curr_node.children:
                        dfs(nr, nc, curr_node)
                        
            # Restore grid cell (Backtrack)
            board[r][c] = char
            
            # Trie Pruning: Remove leaf nodes with no children
            if not curr_node.children:
                parent_node.children.pop(char)
                
        # 3. Scan the grid and trigger DFS from matching start characters
        for r in range(m):
            for c in range(n):
                start_char = board[r][c]
                if start_char in root.children:
                    dfs(r, c, root)
                    
        return res

