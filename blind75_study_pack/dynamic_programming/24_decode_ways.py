from typing import List, Optional, Dict, Set

# Decode Ways - Medium
# 🔑 Key Points: Dynamic Programming - Split Checking with Leading Zeroes
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We want to decode a string of digits `s` where each mapping corresponds to a character (1-26). Similar to climbing stairs, at each step we can decode either 1 digit or 2 digits, but we must validate the ranges (e.g., '0' is invalid on its own, '30' is invalid).
#   - Mathematical Derivation: 
#     Let `dp[i]` be the number of decode ways for prefix `s[0...i-1]`.
#     Recurrence relation:
#     1. If `s[i-1]` is not `'0'`, it can be decoded as a single digit: `dp[i] += dp[i-1]`.
#     2. If the two-digit substring `s[i-2:i]` forms a valid number between `'10'` and `'26'`, it can be decoded as a double digit: `dp[i] += dp[i-2]`.
#     Base cases: `dp[0] = 1`. If the string starts with `'0'`, return 0. We can optimize the space to O(1) using rolling variables.

class Solution:
    def numDecodings(self, s: str) -> int:
        # Time Complexity: O(n) - Single pass loop
        # Space Complexity: O(1) - Two variables for state tracking
        if not s or s[0] == '0':
            return 0
            
        # prev2 acts as dp[i-2], prev1 acts as dp[i-1]
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            # 1. Decode as single digit
            if s[i] != '0':
                current += prev1
            # 2. Decode as double digit
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            prev2 = prev1
            prev1 = current
            
        return prev1

