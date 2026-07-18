from typing import List, Optional, Dict, Set

# Longest Increasing Subsequence (最长递增子序列 - LIS) - Medium
# 🔑 核心考点: 动态规划 O(n^2) / 二分查找搭配贪心策略 O(n log n)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：使用动态规划，设 `dp[i]` 是以 `nums[i]` 结尾的最长递增子序列的长度。对于每个 `nums[i]`，遍历它前面的所有数 `nums[j]`（其中 `j < i`），如果 `nums[i] > nums[j]`，则可以把 `nums[i]` 接在以 `nums[j]` 结尾的子序列后面，状态转移为 `dp[i] = max(dp[i], dp[j] + 1)`。这需要 O(n^2) 时间复杂度。
#   - 思维推导: 
#     为了达到最优的 O(n log n) 复杂度，需要结合贪心和二分查找（耐心理牌算法）：
#     我们维护一个数组 `sub`，其中 `sub[i]` 存储长度为 `i+1` 的最长递增子序列的结尾元素的最小值。
#     遍历 `nums` 中的每个数 `x`：
#     - 如果 `x` 比 `sub` 的最后一个元素还要大，直接将 `x` 添加到 `sub` 尾部。
#     - 否则，我们在 `sub` 中通过二分查找，找到第一个大于或等于 `x` 的元素，并用 `x` 替换它（贪心：越小的结尾元素，越容易在后面接上新的递增数）。
#     最终 `sub` 数组的长度就是所求的最长递增子序列的长度。

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n log n) - 遍历一次数组，每次进行一次二分查找
        空间复杂度: O(n) - 维护 sub 数组
        """
        if not nums:
            return 0
            
        sub = []
        for x in nums:
            # 找到第一个大于或等于 x 的位置
            idx = bisect.bisect_left(sub, x)
            if idx == len(sub):
                sub.append(x)
            else:
                sub[idx] = x
                
        return len(sub)

