from typing import List, Optional, Dict, Set

# House Robber (打家劫舍) - Medium
# 🔑 核心考点: 动态规划 - 间隔选择状态
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：面对一排房子，我们不能抢劫相邻的房子。在每个房子 `i` 前，我们有两个选择：1. 抢劫这间房，那么就不能抢前一间房，最大收益就是之前抢到 `i-2` 房子的最大收益加上当前房子的金额。2. 不抢这间房，那么最大收益就是抢到前一间房 `i-1` 的最大收益。我们取两者中的最大值。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i]` 为抢劫前 `i` 间房能获得的最大金额。
#     状态转移方程：
#     `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
#     空间优化：由于 `dp[i]` 的计算只取决于前两步的状态，我们可以使用两个滚动变量 `rob1`（相当于 `dp[i-2]`）和 `rob2`（相当于 `dp[i-1]`），在每次遍历时交替更新它们，从而将空间复杂度从 O(N) 降低到 O(1)。

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        时间复杂度: O(N) - 一次遍历
        空间复杂度: O(1) - 滚动变量优化
        """
        # rob1 代表 dp[i-2]，rob2 代表 dp[i-1]
        rob1, rob2 = 0, 0
        
        for num in nums:
            # 决策：是抢这间房子，还是跳过这间房子
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2

