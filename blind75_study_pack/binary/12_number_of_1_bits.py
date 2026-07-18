from typing import List, Optional, Dict, Set

# Number of 1 Bits (位1的个数) - Easy
# 🔑 核心考点: 位运算 (Bit Manipulation) - Brian Kernighan 算法 (n & (n - 1))
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：可以通过循环 32 次，每次将数字右移并判断最低位是否为 1。但这需要固定的 32 次迭代，即使数字中只有一个 1。
#   - 思维推导: 
#     使用 n & (n - 1) 消除最低位的 1：
#     对于任意数 n，n - 1 会将 n 最低位的 1 变成 0，并将其右边的所有 0 变成 1。
#     当我们执行 n & (n - 1) 时，会将最低位的 1 及其右边所有的位都清零，而保持左边的位不变。
#     利用这个特性，我们每次执行 n & (n - 1) 都会且仅会消去一个二进制位中的 1。因此，迭代次数仅等于 1 的个数，效率极高。

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        时间复杂度: O(1) - 最多执行 32 次，实际迭代次数等于二进制中 1 的个数
        空间复杂度: O(1)
        """
        count = 0
        while n:
            # 消除二进制中最右边的 1
            n = n & (n - 1)
            count += 1
        return count

