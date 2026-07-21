class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            # check if it is profitable
            profit = prices[right] - prices[left]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                # if it is not profitable, we move the left pointer to the position of the right pointer
                left = right
            right += 1
        return maxProfit
        