from typing import List, Optional, Dict, Set

# LeetCode 121: Best Time to Buy and Sell Stock - Easy
# 🔗 Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 🔑 Key Points: Greedy / Dynamic Programming - Single Pass
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The brute-force solution calculates the profit for every possible buy-and-sell pair (where sell day > buy day) using nested loops, which takes O(N^2) time complexity.
#   - Mathematical Derivation: 
#     Since you must buy before you can sell, we can solve this in a single pass. While traversing the prices, we maintain two variables: the minimum price seen so far (`min_price`) and the maximum profit achieved (`max_profit`). For each price, we update `min_price` and calculate the potential profit if we sold on that day (`price - min_price`), updating `max_profit` if this potential profit is larger.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')  # Track the minimum price seen so far
        max_profit = 0            # Track the maximum profit seen so far
        for price in prices:
            if price < min_price:
                min_price = price  # Update min price if a lower buying price is found
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit if selling today yields more
        return max_profit

