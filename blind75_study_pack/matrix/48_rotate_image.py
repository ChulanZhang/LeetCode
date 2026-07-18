from typing import List, Optional, Dict, Set

# Rotate Image - Medium
# 🔑 Key Points: In-Place Matrix Transpose + Row Reverse
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To rotate a matrix clockwise by 90 degrees, we could map elements into a new matrix using the index relation `new_matrix[j][n-1-i] = matrix[i][j]`. However, interviews require **in-place** rotation with O(1) space constraint.
#   - Mathematical Derivation: 
#     Using matrix transpose and line reflection:
#     A 90-degree clockwise rotation can be decomposed into two simple geometric steps:
#     1. **Transpose the matrix**: Swap `matrix[i][j]` with `matrix[j][i]` for `j > i`. This turns rows into columns (in reversed order).
#     2. **Reverse each row**: Mirror-flip each row horizontally (`matrix[i].reverse()`).
#     Both steps are performed in-place using two-pointer swaps, requiring O(1) auxiliary space.

from typing import List

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

