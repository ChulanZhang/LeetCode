from typing import List, Optional, Dict, Set

# Sum of Two Integers (两数之和 - 不使用加减号) - Medium
# 🔑 核心考点: 位运算 (Bit Manipulation) - 异或(XOR)求无进位和，与(AND)左移求进位
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：不使用 + 或 -，我们需要在二进制位级别模拟加法器的行为。两个数相加可以拆分为：无进位加法（可以通过 XOR 异或实现）和进位（可以通过 AND 与运算并左移一位实现）。
#   - 思维推导: 
#     对于 a 和 b：
#     1. a ^ b 计算出无进位的和（例如 1+1=0, 1+0=1）。
#     2. (a & b) << 1 计算出进位（只有 1+1 会产生进位，进位向左移一位）。
#     3. 重复这个过程，直到进位为 0。
#     在 Python 中，整数是无限精度的，因此我们需要手动使用 32 位掩码 0xFFFFFFFF 来模拟 32 位有符号整数的溢出和负数行为。

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        时间复杂度: O(1) - 因为在 32 位整数范围内，循环最多执行 32 次
        空间复杂度: O(1)
        """
        # 32位最大正整数
        MAX = 0x7FFFFFFF
        # 32位掩码
        mask = 0xFFFFFFFF
        
        while b != 0:
            # 计算无进位和，并限制在32位内
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
            
        # 如果结果是负数（第31位为1），将其转换为 Python 的负数表示
        return a if a <= MAX else ~(a ^ mask)

