from typing import List, Optional, Dict, Set

# Search in Rotated Sorted Array (搜索旋转排序数组) - Medium
# 🔑 核心考点: 二分查找 / 分段单调性判定
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     旋转数组中检索目标值。若直接遍历复杂度为 O(N)。我们需要利用二分查找达到 O(log N) 复杂度。
#   - 思维推导: 
#     旋转数组有一个特性：如果从中间切开，两半中必然有一半是严格递增的。我们可以比较 nums[left] 和 nums[mid] 来确定哪一半是有序的：
#     1. 如果左半部分有序，我们检查 target 是否在左半部分的单调区间内。如果在，我们收缩 right = mid - 1；否则去右半部分寻找（left = mid + 1）。
#     2. 同理，如果右半部分有序，我们检查 target 是否在右半部单调区间内，收缩边界。如此这般折半查找。

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

