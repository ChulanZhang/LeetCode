from typing import List, Optional, Dict, Set

# Maximum Subarray (最大子数组和) - Medium
# 🔑 核心考点: 动态规划 (Kadane's Algorithm) / 贪心算法
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     暴力枚举所有的子数组起点 i 和终点 j，时间复杂度为 O(N^2)。如果数组中全为负数，初始化最大值需要注意不能直接设为 0，必须设为首个元素或负无穷。
#   - 思维推导: 
#     在遍历到每个位置时，我们需要决定：是要继续累加当前数字，还是以当前数字为新子数组的起点？如果之前的累加和为负数，对后续累加只会起到削减作用，应当舍弃并从当前数重新开始。状态转移方程为：current_sum = max(num, current_sum + num)。并在过程中维护全局最大值。

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

