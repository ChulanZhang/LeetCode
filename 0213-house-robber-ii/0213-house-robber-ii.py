class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            if len(houses) == 1:
                return houses[0]
            
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + houses[i]
                )
            return dp[-1]
        
        rob_first = rob_linear(nums[:-1])
        rob_last = rob_linear(nums[1:])

        return max(rob_first, rob_last)