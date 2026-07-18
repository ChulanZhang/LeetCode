from typing import List, Optional, Dict, Set

# Counting Bits (比特位计数) - Easy
# 🔑 核心考点: 动态规划 (DP) + 位运算 (Bit Manipulation)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：对 0 到 n 的每个数分别计算其二进制中 1 的个数，时间复杂度为 O(n log n) 或 O(32n)。
#   - 思维推导: 
#     为了达到 O(n) 的最优时间复杂度，我们应该利用之前已经计算过的数字的结果（动态规划）。
#     设 dp[i] 为数字 i 的二进制中 1 的个数。
#     1. 奇偶性规律：
#        - 如果 i 是偶数，i 的二进制中 1 的个数与 i // 2 相同（因为偶数相当于 i // 2 左移一位，末尾补 0，不增加 1）。即 dp[i] = dp[i >> 1]。
#        - 如果 i 是奇数，i 的二进制中 1 的个数比 i // 2 多 1（末尾是 1）。即 dp[i] = dp[i >> 1] + 1。
#     2. 统一公式：dp[i] = dp[i >> 1] + (i & 1)。这样我们就可以在 O(1) 的时间内从已有的状态推导出新状态。

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        时间复杂度: O(n) - 遍历一次 0 到 n
        空间复杂度: O(1) - 仅使用输出数组，无额外辅助空间
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # dp[i] 等于 dp[i // 2] 加上 i 的最低位是否为 1
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

