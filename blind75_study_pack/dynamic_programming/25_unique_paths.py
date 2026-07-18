from typing import List, Optional, Dict, Set

# Unique Paths - Medium
# 🔑 Key Points: Grid Dynamic Programming / Space Compression
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Since the robot can only move down or right, any cell `(i, j)` can only be reached from the cell above `(i-1, j)` or the cell to the left `(i, j-1)`. The number of unique paths to `(i, j)` is the sum of paths to these two cells.
#   - Mathematical Derivation: 
#     Let `dp[i][j]` be the number of unique paths to grid cell `(i, j)`.
#     Recurrence relation:
#     `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
#     The first row and column are initialized to 1 because there is only one way to go straight down or right.
#     Space Optimization: Since the current row only depends on the row above and the current row's left cell, we can compress the space to a 1D array of size `n` and update it iteratively via `row[j] = row[j] + row[j-1]`.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity: O(m * n) - Single loop over all grid cells
        # Space Complexity: O(n) - Single row array to accumulate states
        
        # Initialize paths in the first row to 1
        row = [1] * n
        
        # Update row by row
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(1, n):
                # new_row[j] (left cell) + row[j] (cell from row above)
                new_row[j] = row[j] + new_row[j-1]
            row = new_row
            
        return row[n-1]

