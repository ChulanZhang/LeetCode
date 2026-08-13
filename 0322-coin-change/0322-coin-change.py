class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum number of coins needed for make amount i
        # Initialize with infinity
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # from 1 to amount
        for i in range(1, amount + 1):
            # Try all possible coins
            for coin in coins:
                # the remaining amount should be non-negative
                if i >= coin:
                    # transition function
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]

# TC: O(nk) 
# SC: O(n)