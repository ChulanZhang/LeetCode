# Binary category data
PROBLEMS = {
    "11_sum_of_two_integers.py": {
        "title": "Sum of Two Integers (两数之和 - 不使用加减号)",
        "difficulty": "Medium",
        "key_points": "位运算 (Bit Manipulation) - 异或(XOR)求无进位和，与(AND)左移求进位",
        "analysis_intuition": "直觉：不使用 + 或 -，我们需要在二进制位级别模拟加法器的行为。两个数相加可以拆分为：无进位加法（可以通过 XOR 异或实现）和进位（可以通过 AND 与运算并左移一位实现）。",
        "analysis_derivation": "对于 a 和 b：\n1. a ^ b 计算出无进位的和（例如 1+1=0, 1+0=1）。\n2. (a & b) << 1 计算出进位（只有 1+1 会产生进位，进位向左移一位）。\n3. 重复这个过程，直到进位为 0。\n在 Python 中，整数是无限精度的，因此我们需要手动使用 32 位掩码 0xFFFFFFFF 来模拟 32 位有符号整数的溢出和负数行为。",
        "code": """class Solution:
    def getSum(self, a: int, b: int) -> int:
        \"\"\"
        时间复杂度: O(1) - 因为在 32 位整数范围内，循环最多执行 32 次
        空间复杂度: O(1)
        \"\"\"
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
"""
    },
    "12_number_of_1_bits.py": {
        "title": "Number of 1 Bits (位1的个数)",
        "difficulty": "Easy",
        "key_points": "位运算 (Bit Manipulation) - Brian Kernighan 算法 (n & (n - 1))",
        "analysis_intuition": "直觉：可以通过循环 32 次，每次将数字右移并判断最低位是否为 1。但这需要固定的 32 次迭代，即使数字中只有一个 1。",
        "analysis_derivation": "使用 n & (n - 1) 消除最低位的 1：\n对于任意数 n，n - 1 会将 n 最低位的 1 变成 0，并将其右边的所有 0 变成 1。\n当我们执行 n & (n - 1) 时，会将最低位的 1 及其右边所有的位都清零，而保持左边的位不变。\n利用这个特性，我们每次执行 n & (n - 1) 都会且仅会消去一个二进制位中的 1。因此，迭代次数仅等于 1 的个数，效率极高。",
        "code": """class Solution:
    def hammingWeight(self, n: int) -> int:
        \"\"\"
        时间复杂度: O(1) - 最多执行 32 次，实际迭代次数等于二进制中 1 的个数
        空间复杂度: O(1)
        \"\"\"
        count = 0
        while n:
            # 消除二进制中最右边的 1
            n = n & (n - 1)
            count += 1
        return count
"""
    },
    "13_counting_bits.py": {
        "title": "Counting Bits (比特位计数)",
        "difficulty": "Easy",
        "key_points": "动态规划 (DP) + 位运算 (Bit Manipulation)",
        "analysis_intuition": "直觉：对 0 到 n 的每个数分别计算其二进制中 1 的个数，时间复杂度为 O(n log n) 或 O(32n)。",
        "analysis_derivation": "为了达到 O(n) 的最优时间复杂度，我们应该利用之前已经计算过的数字的结果（动态规划）。\n设 dp[i] 为数字 i 的二进制中 1 的个数。\n1. 奇偶性规律：\n   - 如果 i 是偶数，i 的二进制中 1 的个数与 i // 2 相同（因为偶数相当于 i // 2 左移一位，末尾补 0，不增加 1）。即 dp[i] = dp[i >> 1]。\n   - 如果 i 是奇数，i 的二进制中 1 的个数比 i // 2 多 1（末尾是 1）。即 dp[i] = dp[i >> 1] + 1。\n2. 统一公式：dp[i] = dp[i >> 1] + (i & 1)。这样我们就可以在 O(1) 的时间内从已有的状态推导出新状态。",
        "code": """from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        \"\"\"
        时间复杂度: O(n) - 遍历一次 0 到 n
        空间复杂度: O(1) - 仅使用输出数组，无额外辅助空间
        \"\"\"
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # dp[i] 等于 dp[i // 2] 加上 i 的最低位是否为 1
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
"""
    },
    "14_missing_number.py": {
        "title": "Missing Number (丢失的数字)",
        "difficulty": "Easy",
        "key_points": "位运算 (XOR 异或) / 数学求和公式 (Gauss Formula)",
        "analysis_intuition": "直觉：先对数组排序，然后找缺失的数，时间复杂度 O(n log n)。或者使用哈希集合，空间复杂度 O(n)。",
        "analysis_derivation": "我们要寻找 O(n) 时间和 O(1) 空间的最优解。\n方法一（数学求和）：0 到 n 的理论总和是 n * (n + 1) // 2。我们求出这个理论和，再减去数组中实际所有数的和，差值就是缺失的数。但需要防范大数溢出（Python 自动处理大数，但在 C++/Java 中可能需要防范）。\n方法二（异或运算）：异或满足交换律和结合律，且 x ^ x = 0，x ^ 0 = x。\n如果我们把 0 到 n 的所有数字，以及数组中的所有数字全部异或在一起，出现两次的数字都会抵消为 0，最后剩下的值就是只出现了一次的那个缺失数字。这就避免了求和溢出问题。",
        "code": """from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        \"\"\"
        时间复杂度: O(n) - 遍历一次数组
        空间复杂度: O(1)
        \"\"\"
        missing = len(nums)
        for i, num in enumerate(nums):
            # 将索引与数值进行异或
            missing ^= i ^ num
        return missing
"""
    },
    "15_reverse_bits.py": {
        "title": "Reverse Bits (颠倒二进制位)",
        "difficulty": "Easy",
        "key_points": "位运算 (Bit Manipulation) - 分步移位",
        "analysis_intuition": "直觉：循环 32 次。每次取出 n 的最低位，放到结果的对应高位上，然后将 n 右移，将结果左移。",
        "analysis_derivation": "1. 初始化结果 res = 0。\n2. 进行 32 次循环：\n   - res 向左移动一位，腾出最低位：`res <<= 1`。\n   - 取出 n 的最低位并加到 res 的最低位上：`res |= (n & 1)`。\n   - n 向右移动一位：`n >>= 1`。\n这是一种非常通用且直观的位逆转方法，对于 32 位有符号/无符号整数均适用。",
        "code": """class Solution:
    def reverseBits(self, n: int) -> int:
        \"\"\"
        时间复杂度: O(1) - 固定的 32 次迭代
        空间复杂度: O(1)
        \"\"\"
        res = 0
        for _ in range(32):
            # 将结果左移，并把 n 的最低位加到结果中
            res = (res << 1) | (n & 1)
            # n 右移一位，准备处理下一位
            n >>= 1
        return res
"""
    }
}
