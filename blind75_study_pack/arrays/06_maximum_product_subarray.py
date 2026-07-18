from typing import List, Optional, Dict, Set

# Maximum Product Subarray (乘积最大子数组) - Medium
# 🔑 核心考点: 动态规划 / 双状态维护（最大与最小值应对负负得正）
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     与最大子数组和不同，乘法中存在“负负得正”。如果之前有一个很大的负数，再乘以一个负数就会变成极大的正数。因此如果只维护最大值，会丢失潜在的最优解。
#   - 思维推导: 
#     我们必须同时维护当前位置的“最大乘积”和“最小乘积”（绝对值很大的负数）。每到一个位置，我们通过当前数、当前数乘上最大积、当前数乘上最小积这三者，分别更新当前位置的最大乘积和最小乘积，从而在 O(N) 时间和 O(1) 空间下得出全局最大乘积。

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        cur_min = nums[0]
        cur_max = nums[0]
        for num in nums[1:]:
            temp = cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)
            res = max(res, cur_max)
        return res

