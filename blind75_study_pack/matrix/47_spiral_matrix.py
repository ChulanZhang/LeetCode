from typing import List, Optional, Dict, Set

# LeetCode 54: Spiral Matrix - Medium
# 🔗 Link: https://leetcode.com/problems/spiral-matrix/
# 🔑 Key Points: Matrix Boundary Simulation
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to return all elements of the matrix in spiral (clockwise) order. This is a simulation task. We can maintain four boundaries (top, bottom, left, right) and shrink them as we complete traversal directions.
#   - Mathematical Derivation: 
#     1. Initialize the boundaries: `top = 0`, `bottom = m - 1`, `left = 0`, `right = n - 1`.
#     2. While `left <= right` and `top <= bottom`:
#        - **Go right**: Traverse the top row from left to right, then increment `top`.
#        - **Go down**: Traverse the right column from top to bottom, then decrement `right`.
#        - **Go left**: (Verify `top <= bottom` first to prevent duplicate processing of a single row) Traverse the bottom row from right to left, then decrement `bottom`.
#        - **Go up**: (Verify `left <= right` first to prevent duplicate processing of a single column) Traverse the left column from bottom to top, then increment `left`.
#     3. The simulation naturally terminates when boundaries overlap.

from typing import List

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

