from typing import List, Optional, Dict, Set

# Word Search - Medium
# 🔑 Key Points: Backtracking / DFS
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to find if a word path exists in a grid. Since we cannot reuse the same cell twice in a single path, this is a path search in an undirected graph. We scan for matching first letters, then initiate DFS.
#   - Mathematical Derivation: 
#     1. Iterate through each cell `(r, c)`. If `grid[r][c] == word[0]`, initiate DFS `dfs(r, c, 0)` where the index `0` represents the matching character index in the word.
#     2. DFS logic `dfs(r, c, index)`:
#        - **Base case**: If `index == len(word)`, the word is fully matched. Return True.
#        - **Pruning**: If `(r, c)` is out of bounds, already visited, or `grid[r][c] != word[index]`, return False.
#        - **Mark visited**: Temporarily mark the cell as visited by overwriting it with a special character (e.g. `'#'`). This avoids using a visited set.
#        - **Four-directional search**: Recursively call DFS in four directions for `index + 1`. If any direction returns True, path exists.
#        - **Backtrack**: Restore the original character to the cell (unmarking it) before returning.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time Complexity: O(M * N * 3^L) - M, N are dimensions, L is word length. At each cell, we explore 3 branches (excluding the parent path)
        # Space Complexity: O(L) - Maximum recursion stack depth equals word length L
        m, n = len(board), len(board[0])
        
        def dfs(r, c, index):
            # All letters matched successfully
            if index == len(word):
                return True
                
            # Boundary check and character match check
            if (r < 0 or r >= m or c < 0 or c >= n or 
                board[r][c] != word[index]):
                return False
                
            # Temporarily mark current cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Search adjacent cells recursively
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
                     
            # Restore original character (Backtracking)
            board[r][c] = temp
            
            return found
            
        for r in range(m):
            for c in range(n):
                # Trigger search from cells matching the first letter
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False

