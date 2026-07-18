from typing import List, Optional, Dict, Set

# Missing Number (丢失的数字) - Easy
# 🔑 核心考点: 位运算 (XOR 异或) / 数学求和公式 (Gauss Formula)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：先对数组排序，然后找缺失的数，时间复杂度 O(n log n)。或者使用哈希集合，空间复杂度 O(n)。
#   - 思维推导: 
#     我们要寻找 O(n) 时间和 O(1) 空间的最优解。
#     方法一（数学求和）：0 到 n 的理论总和是 n * (n + 1) // 2。我们求出这个理论和，再减去数组中实际所有数的和，差值就是缺失的数。但需要防范大数溢出（Python 自动处理大数，但在 C++/Java 中可能需要防范）。
#     方法二（异或运算）：异或满足交换律和结合律，且 x ^ x = 0，x ^ 0 = x。
#     如果我们把 0 到 n 的所有数字，以及数组中的所有数字全部异或在一起，出现两次的数字都会抵消为 0，最后剩下的值就是只出现了一次的那个缺失数字。这就避免了求和溢出问题。

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        时间复杂度: O(n) - 遍历一次数组
        空间复杂度: O(1)
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            # 将索引与数值进行异或
            missing ^= i ^ num
        return missing

