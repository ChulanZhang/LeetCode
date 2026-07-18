from typing import List, Optional, Dict, Set

# Best Time to Buy and Sell Stock (买卖股票的最佳时机) - Easy
# 🔑 核心考点: 贪心算法 (Greedy) / 动态规划状态简化 - 一次遍历
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     暴力解法是计算所有可能的买入和卖出组合（即双重循环，外层买入，内层卖出且卖出在买入之后），寻找最大的差值，时间复杂度为 O(N^2)。
#   - 思维推导: 
#     由于你必须先买入，才能卖出，不能简单地找出数组的最小值和最大值然后相减（因为最大值可能出现在最小值之前）。我们在遍历数组时，可以实时维护一个“历史最低买入价” min_price，以及“历史最大利润” max_profit。当我们在第 i 天卖出股票，最大利润就是价格差 price - min_price。我们用它去更新 max_profit 即可。

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

