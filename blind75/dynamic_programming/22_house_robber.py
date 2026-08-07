from typing import List, Optional, Dict, Set

# LeetCode 198: House Robber - Medium
# 🔗 Link: https://leetcode.com/problems/house-robber/
# 🔑 Key Points: Dynamic Programming - Space Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     When robbing houses, we cannot rob adjacent ones. At house `i`, we have two options: 1. Rob this house, meaning we cannot rob house `i-1`. The max profit is `dp[i-2] + nums[i]`. 2. Skip this house, meaning we keep the max profit from house `i-1`, which is `dp[i-1]`. We choose the maximum of these two options.
#   - Mathematical Derivation: 
#     Let `dp[i]` be the max amount we can rob from the first `i` houses.
#     Recurrence relation:
#     `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
#     Space Optimization: Since `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`, we can use two variables `rob1` (representing `dp[i-2]`) and `rob2` (representing `dp[i-1]`) to scroll forward, optimizing space from O(N) to O(1).

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(N) - Single pass loop
        # Space Complexity: O(1) - Two variables scroll state
        
        # rob1 acts as dp[i-2], rob2 acts as dp[i-1]
        rob1, rob2 = 0, 0
        
        for num in nums:
            # Choose between robbing current house + rob1, or skipping it (rob2)
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2

