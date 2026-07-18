from typing import List, Optional, Dict, Set

# Set Matrix Zeroes - Medium
# 🔑 Key Points: Matrix In-Place Marking - O(1) Space Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to set rows and columns to 0 if a cell contains 0. Modifying elements directly during the scan will corrupt state detection for downstream cells, causing the whole grid to turn to 0. Creating external row/column arrays requires O(M + N) space. How can we optimize this to O(1)?
#   - Mathematical Derivation: 
#     We can use the **first row and first column** of the matrix itself as the state markers:
#     1. Check if the first row and column initially contain any 0s, saving this state in two boolean flags `first_row_zero` and `first_col_zero`.
#     2. Iterate through the rest of the matrix (excluding the first row and column). If `matrix[r][c] == 0`, set its projection markers `matrix[r][0] = 0` and `matrix[0][c] = 0`.
#     3. Iterate through the sub-grid again. If row marker `matrix[r][0] == 0` or column marker `matrix[0][c] == 0` is set, change `matrix[r][c]` to 0.
#     4. Finally, use the boolean flags to zero out the first row and column if necessary. This achieves O(1) auxiliary space.

from typing import List

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

