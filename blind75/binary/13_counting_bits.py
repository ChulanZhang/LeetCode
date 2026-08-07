from typing import List, Optional, Dict, Set

# LeetCode 338: Counting Bits - Easy
# 🔗 Link: https://leetcode.com/problems/counting-bits/
# 🔑 Key Points: Dynamic Programming + Bit Manipulation
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Calculating the number of set bits for each number from 0 to n individually takes O(N log N) or O(32N) time complexity.
#   - Mathematical Derivation: 
#     To achieve an optimal O(N) time complexity, we can use dynamic programming by reusing previously computed results.
#     Let `dp[i]` be the count of 1 bits in the binary representation of `i`.
#     1. Parity rules:
#        - If `i` is even, `dp[i] = dp[i >> 1]` because dividing an even number by 2 is a right shift that discards a 0 bit (no change in 1s count).
#        - If `i` is odd, `dp[i] = dp[i >> 1] + 1` because dividing an odd number by 2 is a right shift that discards a 1 bit (adds 1 to the count).
#     2. Unified recurrence: `dp[i] = dp[i >> 1] + (i & 1)`. This allows us to compute each state in O(1) time.

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time Complexity: O(n) - Single pass from 0 to n
        # Space Complexity: O(1) - Only the output array is allocated
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # Recurrence: set bits in i equals set bits in i // 2 + LSB of i
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

