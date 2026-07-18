from typing import List, Optional, Dict, Set

# Two Sum (两数之和) - Easy
# 🔑 核心考点: 哈希表 (Hash Map) - 空间换时间
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     最容易想到的暴力方法是双重循环（Nested Loops），外层固定元素 A，内层在其余元素中寻找 B 使得 A + B = target。时间复杂度是 O(N^2)。在面试中是无法接受的，尤其是当数组规模达到 10^4 以上时，会直接超时。且要注意避开同一个元素重复使用和重复数值的处理这两个边界。
#   - 思维推导: 
#     为了将复杂度降低到 O(N)，我们需要在一边遍历数组的过程中，一边把已经访问过的元素及其索引存入哈希表中。这样，对于下一个数，我们只需在哈希表中检索它的互补数是否存在即可。利用哈希表进行 O(1) 复杂度的查找。

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            num_to_idx[num] = i
        return []

