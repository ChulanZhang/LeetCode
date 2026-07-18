from typing import List, Optional, Dict, Set

# Longest Consecutive Sequence (最长连续序列) - Medium
# 🔑 核心考点: 哈希集合 (Hash Set) - O(N) 突破排序限制
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：最简单的方法是将数组排序，然后线性扫描寻找最长连续段，但这需要 O(N log N) 的时间复杂度。题目要求我们设计一个时间复杂度为 O(N) 的算法。
#   - 思维推导: 
#     为了在不排序的前提下，在 O(N) 时间内找出最长连续段，我们可以利用哈希集合（查询复杂度为 O(1)）：
#     1. 将所有数字存入哈希集合 `num_set`。
#     2. 遍历集合中的每一个数 `num`：
#        - **破局点**：如何避免对同一个序列中的每个数字重复计数？我们只需要在遇到**序列的起点**时才开始向后累加。如何判断 `num` 是不是起点？如果 `num - 1` 不在集合中，说明没有比它小 1 的数，那么它就是这个连续序列的起点。
#        - 找到起点后，我们用一个循环不断判断 `num + 1`，`num + 2`... 是否在集合中，从而统计出该序列的长度。
#     虽然内部有一个 `while` 循环，但由于我们限定了只有“起点”才会触发 `while` 循环，所以每个数字最多只会被访问两次（一次在外部遍历中，一次在 `while` 累加中）。因此，总时间复杂度依然是严格的 O(N)。

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        时间复杂度: O(N) - 每个数字最多被处理常数次
        空间复杂度: O(N) - 存储哈希集合
        """
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # 只有当 num - 1 不在集合中时，num 才是某段连续序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # 沿起点向后累加
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak

