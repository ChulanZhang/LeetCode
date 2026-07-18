from typing import List, Optional, Dict, Set

# Combination Sum IV - Medium
# 🔑 Key Points: Unbounded Knapsack Permutations / Dynamic Programming
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     This is similar to the Coin Change problem but asks for the number of combinations (permutations where different orders count as distinct). For example, if `nums = [1, 2, 3]` and `target = 4`, `(1, 3)` and `(3, 1)` are distinct. Because order matters, we iterate over the targets in the outer loop, and over the numbers in the inner loop.
#   - Mathematical Derivation: 
#     Let `dp[i]` be the number of permutations that sum to `i`.
#     To make a sum of `i`, we can choose any number `num` from `nums` (where `i >= num`) as the last element. The number of permutations is then the sum of `dp[i - num]` for all choices of `num`:
#     `dp[i] = sum(dp[i - num] for num in nums)`
#     Base case: `dp[0] = 1` (one way to form sum 0, i.e., empty set).

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(target * n) - target is the target sum, n is the size of nums
        # Space Complexity: O(target)
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to make sum 0
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]

