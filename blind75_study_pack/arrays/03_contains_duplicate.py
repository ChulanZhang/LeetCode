from typing import List, Optional, Dict, Set

# Contains Duplicate (存在重复元素) - Easy
# 🔑 核心考点: 哈希集合 (Hash Set) - 早期终止优化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     暴力解法是双重循环，依次两两比对，时间复杂度为 O(N^2)。如果直接使用 Python 的 len(set(nums)) != len(nums)，大数组下，无法早期终止（Early Return）可能会导致不必要的性能浪费。
#   - 思维推导: 
#     在允许使用额外空间的前提下，为了达到 O(N) 的时间复杂度，我们可以使用哈希集合 visited。一边遍历数组，一边把遇到的数字放入 visited 中。每次放入前先检查它是否已经在 visited 中。如果在，说明找到了重复元素，直接返回 True 早期终止。

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False

