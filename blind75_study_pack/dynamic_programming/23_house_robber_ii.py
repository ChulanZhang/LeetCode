from typing import List, Optional, Dict, Set

# House Robber II (打家劫舍 Ⅱ) - Medium
# 🔑 核心考点: 环形数组动态规划
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：这道题和上一题的唯一区别在于房子的排列从一排变成了一个环，这意味着第一间房和最后一间房相邻，不能同时被抢。
#   - 思维推导: 
#     为了破开环形依赖，我们可以把问题拆分为两个线性的子问题：
#     1. 如果我们抢了第一间房，我们就绝对不能抢最后一间房。此时问题简化为在第 1 间房到第 n-1 间房中进行正常的线性抢劫规划。
#     2. 如果我们不抢第一间房，我们就可以选择抢最后一间房。此时问题简化为在第 2 间房到第 n 间房中进行正常的线性抢劫规划。
#     由于所有可能的最优解必然落在这两种情况之中，我们只需要对这两段子区间分别运行一次线性“打家劫舍”的求解器，并取最大值即可。注意边界情况：若只有 1 间房，直接返回其价值。

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        时间复杂度: O(N) - 运行两次线性打家劫舍，均为 O(N)
        空间复杂度: O(1)
        """
        if len(nums) == 1:
            return nums[0]
            
        # 线性打家劫舍辅助函数
        def rob_linear(house_prices: List[int]) -> int:
            rob1, rob2 = 0, 0
            for price in house_prices:
                temp = max(rob1 + price, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # 结果为：不包含最后一间房的最大值 与 不包含第一间房的最大值 中的较大者
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

