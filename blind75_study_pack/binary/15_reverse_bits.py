from typing import List, Optional, Dict, Set

# Reverse Bits (颠倒二进制位) - Easy
# 🔑 核心考点: 位运算 (Bit Manipulation) - 分步移位
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：循环 32 次。每次取出 n 的最低位，放到结果的对应高位上，然后将 n 右移，将结果左移。
#   - 思维推导: 
#     1. 初始化结果 res = 0。
#     2. 进行 32 次循环：
#        - res 向左移动一位，腾出最低位：`res <<= 1`。
#        - 取出 n 的最低位并加到 res 的最低位上：`res |= (n & 1)`。
#        - n 向右移动一位：`n >>= 1`。
#     这是一种非常通用且直观的位逆转方法，对于 32 位有符号/无符号整数均适用。

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        时间复杂度: O(1) - 固定的 32 次迭代
        空间复杂度: O(1)
        """
        res = 0
        for _ in range(32):
            # 将结果左移，并把 n 的最低位加到结果中
            res = (res << 1) | (n & 1)
            # n 右移一位，准备处理下一位
            n >>= 1
        return res

