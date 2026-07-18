from typing import List, Optional, Dict, Set

# House Robber II - Medium
# 🔑 Key Points: Circular Array Dynamic Programming
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The only difference from House Robber I is that the houses are arranged in a circle, meaning the first house and the last house are adjacent and cannot be robbed together.
#   - Mathematical Derivation: 
#     To break this circular constraint, we can split the problem into two linear subproblems:
#     1. If we rob the first house, we cannot rob the last house. The problem simplifies to a linear scan of houses `[0...n-2]`.
#     2. If we skip the first house, we can potentially rob the last house. The problem simplifies to a linear scan of houses `[1...n-1]`.
#     Since the optimal solution must fall in one of these two categories, we run the linear solver on both sub-arrays and return the maximum of the two. Base case: if there is only 1 house, return its value directly.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(N) - Linear scans of arrays of size N-1
        # Space Complexity: O(1)
        if len(nums) == 1:
            return nums[0]
            
        # Helper to compute linear house robber
        def rob_linear(house_prices: List[int]) -> int:
            rob1, rob2 = 0, 0
            for price in house_prices:
                temp = max(rob1 + price, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # Take the maximum of skipping the last house, and skipping the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

