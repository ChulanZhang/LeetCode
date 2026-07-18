from typing import List, Optional, Dict, Set

# Decode Ways (解码方法) - Medium
# 🔑 核心考点: 划分动态规划 / 边界与前导零处理
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：输入一个由数字组成的字符串 `s`，我们想要把它拆分成字符解码。这类似于爬楼梯问题，我们每一步可以选择解码 1 个数字，或者解码 2 个数字，但由于数字代表字符（1-26），存在有效性的限制（例如 '0' 无法单独解码，'30' 无法被解码等）。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i]` 为字符串前 `i` 个字符构成的子串的解码方法总数。
#     状态转移方程：
#     1. 如果 `s[i-1]` 不为 `'0'`，那么它可以单独作为一个字符解码：`dp[i] += dp[i-1]`。
#     2. 如果双位数 `s[i-2:i]` 在 `'10'` 到 `'26'` 之间，那么它可以作为两个数字的组合解码：`dp[i] += dp[i-2]`。
#     初始条件：`dp[0] = 1`（空字符串有 1 种解码方式）。如果字符串以 `'0'` 开头，直接返回 0。我们可以使用滚动变量将空间优化至 O(1)。

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        时间复杂度: O(n) - n 为 s 的长度，遍历一次
        空间复杂度: O(1) - 滚动变量优化
        """
        if not s or s[0] == '0':
            return 0
            
        # prev2 代表 dp[i-2]，prev1 代表 dp[i-1]
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            # 1. 尝试以单个数字解码
            if s[i] != '0':
                current += prev1
            # 2. 尝试以双位数字解码
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            prev2 = prev1
            prev1 = current
            
        return prev1

