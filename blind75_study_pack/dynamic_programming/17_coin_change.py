from typing import List, Optional, Dict, Set

# Coin Change (零钱兑换) - Medium
# 🔑 核心考点: 完全背包问题 / 动态规划
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：使用贪心策略，优先使用面值最大的硬币。但这种策略对于某些组合不成立。例如 coins = [1, 3, 4], amount = 6，贪心策略会选 4 + 1 + 1 (3枚)，但最优解是 3 + 3 (2枚)。因此必须枚举所有可能的状态，求最优解。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i]` 为凑齐金额 `i` 所需的最少硬币数。
#     状态转移方程：
#     对于凑齐金额 `i`，我们可以尝试使用任何一枚硬币 `coin`。如果使用这枚硬币，剩余需要凑齐的金额就是 `i - coin`。那么此时的最少硬币数就是 `dp[i - coin] + 1`。
#     我们需要在所有可用的硬币中取最小值：
#     `dp[i] = min(dp[i], dp[i - coin] + 1)` 满足 `i >= coin` 且 `dp[i - coin]` 有效。
#     自底向上循环计算，初始化 `dp[0] = 0`，其余设为无穷大。最后检查 `dp[amount]` 是否仍然为无穷大（代表无法凑齐）。

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        时间复杂度: O(n * amount) - n 为硬币种类数，内层循环为硬币遍历
        空间复杂度: O(amount) - DP 数组大小为 amount + 1
        """
        # 初始化为 amount + 1，相当于正无穷大（因为最多使用 amount 枚 1 元硬币）
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

