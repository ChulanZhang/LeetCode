from typing import List, Optional, Dict, Set

# Climbing Stairs (爬楼梯) - Easy
# 🔑 核心考点: 动态规划 (DP) / 斐波那契数列 (Fibonacci)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要爬到第 n 阶，最后一步要么是从第 n-1 阶跨了 1 步，要么是从第 n-2 阶跨了 2 步。所以，爬到第 n 阶的方法数就是爬到第 n-1 阶的方法数与爬到第 n-2 阶的方法数之和。这显然是斐波那契数列的关系。
#   - 思维推导: 
#     状态转移方程：
#     `dp[i] = dp[i-1] + dp[i-2]`
#     由于计算 `dp[i]` 只需要前两个状态，我们不需要维持一个完整的 dp 数组，而是可以用两个变量 `one` 和 `two` 来交替滚动更新，将空间复杂度从 O(n) 降低到 O(1)。

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        时间复杂度: O(n) - 线性扫描一次
        空间复杂度: O(1) - 仅使用两个状态变量
        """
        if n <= 2:
            return n
            
        # one 代表 dp[i-1]，two 代表 dp[i-2]
        one, two = 1, 2
        for _ in range(3, n + 1):
            temp = one + two
            one = two
            two = temp
            
        return two

