from typing import List, Optional, Dict, Set

# LeetCode 1143: Longest Common Subsequence - Medium
# 🔗 Link: https://leetcode.com/problems/longest-common-subsequence/
# 🔑 Key Points: 2D Dynamic Programming (2D DP)
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To find the longest common subsequence of `text1` and `text2`, we can compare characters from the ends. If they match, they can be part of the LCS. If they don't, we can try skipping the last character of either `text1` or `text2` and take the maximum.
#   - Mathematical Derivation: 
#     Let `dp[i][j]` be the length of the LCS of `text1[0...i-1]` and `text2[0...j-1]`.
#     State transition:
#     1. If `text1[i - 1] == text2[j - 1]`, the characters match: `dp[i][j] = dp[i - 1][j - 1] + 1`.
#     2. If `text1[i - 1] != text2[j - 1]`, they do not match: `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`.
#     We create a 2D matrix of size `(m+1) * (n+1)` initialized to 0. We fill the matrix bottom-up, and `dp[m][n]` yields the result.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Complexity: O(m * n) - Fill the 2D DP matrix
        # Space Complexity: O(m * n) - Size of the 2D DP matrix
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Match found: diagonal value + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match: take max of left and top values
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]

