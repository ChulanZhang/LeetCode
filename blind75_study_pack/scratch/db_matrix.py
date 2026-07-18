# Matrix category data
PROBLEMS = {
    "46_set_matrix_zeroes.py": {
        "title": "Set Matrix Zeroes",
        "difficulty": "Medium",
        "key_points": "Matrix In-Place Marking - O(1) Space Optimization",
        "analysis_intuition": "We need to set rows and columns to 0 if a cell contains 0. Modifying elements directly during the scan will corrupt state detection for downstream cells, causing the whole grid to turn to 0. Creating external row/column arrays requires O(M + N) space. How can we optimize this to O(1)?",
        "analysis_derivation": "We can use the **first row and first column** of the matrix itself as the state markers:\n1. Check if the first row and column initially contain any 0s, saving this state in two boolean flags `first_row_zero` and `first_col_zero`.\n2. Iterate through the rest of the matrix (excluding the first row and column). If `matrix[r][c] == 0`, set its projection markers `matrix[r][0] = 0` and `matrix[0][c] = 0`.\n3. Iterate through the sub-grid again. If row marker `matrix[r][0] == 0` or column marker `matrix[0][c] == 0` is set, change `matrix[r][c]` to 0.\n4. Finally, use the boolean flags to zero out the first row and column if necessary. This achieves O(1) auxiliary space.",
        "code": """from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        # Time Complexity: O(M * N) - Two passes over the matrix
        # Space Complexity: O(1) - Mark state stored in first row and first column
        if not matrix:
            return
            
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # 1. Determine if the first row or first column has any zero initially
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_zero = True
                break
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_zero = True
                break
                
        # 2. Iterate rest of the cells and store the zero states in the first row and column
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # 3. Use the marks in the first row/col to zero out cells in the sub-matrix
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # 4. Separately zero out the first row and first column if needed
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0
"""
    },
    "47_spiral_matrix.py": {
        "title": "Spiral Matrix",
        "difficulty": "Medium",
        "key_points": "Matrix Boundary Simulation",
        "analysis_intuition": "We need to return all elements of the matrix in spiral (clockwise) order. This is a simulation task. We can maintain four boundaries (top, bottom, left, right) and shrink them as we complete traversal directions.",
        "analysis_derivation": "1. Initialize the boundaries: `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.\n2. While `left <= right` and `top <= bottom`:\n   - **Go right**: Traverse the top row from left to right, then increment `top`.\n   - **Go down**: Traverse the right column from top to bottom, then decrement `right`.\n   - **Go left**: (Verify `top <= bottom` first to prevent duplicate processing of a single row) Traverse the bottom row from right to left, then decrement `bottom`.\n   - **Go up**: (Verify `left <= right` first to prevent duplicate processing of a single column) Traverse the left column from bottom to top, then increment `left`.\n3. The simulation naturally terminates when boundaries overlap.",
        "code": """from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time Complexity: O(M * N) - Each cell is visited exactly once
        # Space Complexity: O(1) - Traversal pointer state uses constant space
        if not matrix:
            return []
            
        m, n = len(matrix), len(matrix[0])
        res = []
        
        # Define boundaries
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while left <= right and top <= bottom:
            # 1. Traverse from left to right along top boundary
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. Traverse from top to bottom along right boundary
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # 3. Traverse from right to left along bottom boundary
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
                
            if left <= right:
                # 4. Traverse from bottom to top along left boundary
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
                
        return res
"""
    },
    "48_rotate_image.py": {
        "title": "Rotate Image",
        "difficulty": "Medium",
        "key_points": "In-Place Matrix Transpose + Row Reverse",
        "analysis_intuition": "To rotate a matrix clockwise by 90 degrees, we could map elements into a new matrix using the index relation `new_matrix[j][n-1-i] = matrix[i][j]`. However, interviews require **in-place** rotation with O(1) space constraint.",
        "analysis_derivation": "Using matrix transpose and line reflection:\nA 90-degree clockwise rotation can be decomposed into two simple geometric steps:\n1. **Transpose the matrix**: Swap `matrix[i][j]` with `matrix[j][i]` for `j > i`. This turns rows into columns (in reversed order).\n2. **Reverse each row**: Mirror-flip each row horizontally (`matrix[i].reverse()`).\nBoth steps are performed in-place using two-pointer swaps, requiring O(1) auxiliary space.",
        "code": """from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        # Time Complexity: O(N^2) - N is matrix dimension. Transpose and reverse take O(N^2) combined
        # Space Complexity: O(1) - Pointers modified in-place
        n = len(matrix)
        
        # 1. Transpose the matrix: Swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. Reverse each row horizontally
        for i in range(n):
            matrix[i].reverse()
"""
    },
    "49_word_search.py": {
        "title": "Word Search",
        "difficulty": "Medium",
        "key_points": "Backtracking / DFS",
        "analysis_intuition": "We need to find if a word path exists in a grid. Since we cannot reuse the same cell twice in a single path, this is a path search in an undirected graph. We scan for matching first letters, then initiate DFS.",
        "analysis_derivation": "1. Iterate through each cell `(r, c)`. If `grid[r][c] == word[0]`, initiate DFS `dfs(r, c, 0)` where the index `0` represents the matching character index in the word.\n2. DFS logic `dfs(r, c, index)`:\n   - **Base case**: If `index == len(word)`, the word is fully matched. Return True.\n   - **Pruning**: If `(r, c)` is out of bounds, already visited, or `grid[r][c] != word[index]`, return False.\n   - **Mark visited**: Temporarily mark the cell as visited by overwriting it with a special character (e.g. `'#'`). This avoids using a visited set.\n   - **Four-directional search**: Recursively call DFS in four directions for `index + 1`. If any direction returns True, path exists.\n   - **Backtrack**: Restore the original character to the cell (unmarking it) before returning.",
        "code": """from typing import List

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
"""
    }
}
