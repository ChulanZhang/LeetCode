from typing import List, Optional, Dict, Set

# Product of Array Except Self (除自身以外数组的乘积) - Medium
# 🔑 核心考点: 前缀乘积与后缀乘积 (Prefix & Suffix Products) / 空间优化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     最直观的方法是把所有数乘起来得到 total_product，然后除以每个位置的 nums[i]。但题目要求不能使用除法，且如果数组中包含 0 会导致除以 0 的错误。
#   - 思维推导: 
#     除了自身之外的所有元素积，可以拆分为：当前元素左边所有数的乘积（前缀积）乘上右边所有数的乘积（后缀积）。我们可以直接用返回的 answer 数组暂存前缀积。接着，反向扫描数组，用一个变量 suffix_product 动态维护右侧乘积，并在遍历过程中乘到对应的位置上，这样实现 O(1) 额外空间。

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        return answer

