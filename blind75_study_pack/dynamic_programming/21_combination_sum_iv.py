from typing import List, Optional, Dict, Set

# Combination Sum IV (组合总和 Ⅳ) - Medium
# 🔑 核心考点: 完全背包排列数 / 动态规划
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：本题与“零钱兑换”有些类似，但它求的是**组合的个数（实际上因为顺序不同算作不同组合，所以是排列数）**。例如 nums = [1, 2, 3], target = 4，(1, 3) 和 (3, 1) 被算作两种不同的结果。由于顺序敏感，我们在状态转移时应当将当前物品的循环放在内层。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i]` 为组合成目标整数 `i` 的排列个数。
#     状态转移方程：
#     为了凑成总和 `i`，我们可以选择数组 `nums` 中的任意一个数 `num` 作为排列的最后一个数。那么在此之前我们需要凑出的总和就是 `i - num`。
#     因此，凑成 `i` 的所有方法数就是所有满足 `i >= num` 的 `dp[i - num]` 之和。
#     公式：
#     `dp[i] = sum(dp[i - num] for num in nums)`
#     基础情况：`dp[0] = 1`（凑出 0 的方法只有一种，即什么数都不选）。

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        时间复杂度: O(target * n) - target 为目标和，n 为数组大小
        空间复杂度: O(target)
        """
        dp = [0] * (target + 1)
        dp[0] = 1  # 基础状态，凑成和为 0 的排列数只有 1 种
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]

