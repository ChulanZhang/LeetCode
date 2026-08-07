from typing import List, Optional, Dict, Set

# LeetCode 152: Maximum Product Subarray - Medium
# 🔗 Link: https://leetcode.com/problems/maximum-product-subarray/
# 🔑 Key Points: Dynamic Programming - Double State Tracking
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Unlike the subarray sum problem, multiplication supports 'two negatives make a positive'. A very small negative number can become a large positive number when multiplied by another negative. Thus, tracking only the maximum product is insufficient.
#   - Mathematical Derivation: 
#     We must maintain both the current maximum product and the current minimum product (which could be a large negative number). For each element, we calculate the potential new max and min by comparing the current number, current number * prev_max, and current number * prev_min. This allows us to handle sign flips in O(N) time and O(1) space.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        cur_min = nums[0]  # Minimum product seen ending at current index
        cur_max = nums[0]  # Maximum product seen ending at current index
        
        for num in nums[1:]:
            temp = cur_max
            # Update current max and min considering possible sign changes
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)
            res = max(res, cur_max)
            
        return res

