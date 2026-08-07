from typing import List, Optional, Dict, Set

# LeetCode 322: Coin Change - Medium
# 🔗 Link: https://leetcode.com/problems/coin-change/
# 🔑 Key Points: Complete Knapsack Problem / Dynamic Programming
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A greedy strategy of choosing the largest denomination coin first fails for many combinations. For example, if `coins = [1, 3, 4]` and `amount = 6`, greedy selects `4 + 1 + 1` (3 coins), whereas the optimal selection is `3 + 3` (2 coins). Thus, we must evaluate all combinations using dynamic programming.
#   - Mathematical Derivation: 
#     Let `dp[i]` be the minimum number of coins needed to make up amount `i`.
#     To calculate `dp[i]`, we can try taking any coin of value `coin` (where `i >= coin`). If we take that coin, the remaining amount is `i - coin`. The coin count becomes `dp[i - coin] + 1`.
#     We take the minimum over all available coins:
#     `dp[i] = min(dp[i], dp[i - coin] + 1)`
#     We initialize `dp[0] = 0` and all other entries to infinity (or `amount + 1`). Finally, we check if `dp[amount]` remains at `amount + 1` (meaning it's unreachable).

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity: O(n * amount) - n is the number of coin denominations
        # Space Complexity: O(amount) - DP array size is amount + 1
        
        # Initialize with amount + 1 representing infinity
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Choose minimum between not using this coin and using this coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

