from typing import List, Optional, Dict, Set

# LeetCode 139: Word Break - Medium
# 🔗 Link: https://leetcode.com/problems/word-break/
# 🔑 Key Points: Dynamic Programming - Substring Checking via Hash Set
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A naive DFS recursively partitions `s` by matching words from `wordDict`. However, without memoization, this yields exponential time complexity due to redundant subproblem checks. We must use dynamic programming.
#   - Mathematical Derivation: 
#     Let `dp[i]` be a boolean indicating whether the prefix `s[0...i-1]` can be segmented into words from `wordDict`.
#     State transition:
#     To calculate `dp[i]`, we check all partitioning splits `j` (where `0 <= j < i`). If `dp[j]` is True (meaning prefix `s[0...j-1]` is valid) and the suffix `s[j...i-1]` is present in the dictionary, then `dp[i]` becomes True.
#     Formula: `dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`.
#     Base case: `dp[0] = True` (empty string is always valid). Output is `dp[len(s)]`.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time Complexity: O(n^2) - Outer loop n steps, inner loop checks up to n divisions
        # Space Complexity: O(n + m) - DP array size n, wordSet size m
        word_set = set(wordDict)  # O(1) average lookup time
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string is segmentable
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If prefix s[:j] is valid and suffix s[j:i] is in dict
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid partition, skip further checks for index i
                    
        return dp[len(s)]

