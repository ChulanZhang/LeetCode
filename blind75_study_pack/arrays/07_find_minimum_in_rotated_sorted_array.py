from typing import List, Optional, Dict, Set

# Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值) - Medium
# 🔑 核心考点: 二分查找 (Binary Search)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     在一个旋转过的升序数组中找最小值。直接遍历需要 O(N) 的时间。因为原本是有序的，我们需要在 O(log N) 的时间内解决。
#   - 思维推导: 
#     使用二分查找。如果中间值 nums[mid] 大于右边界 nums[right]，说明旋转折返点在 mid 的右半边，最小值必定在 mid + 1 到 right 之间，因此 left = mid + 1。否则，说明右半边是单调递增的，最小值可能是 mid 本身或者在左半边，因此 right = mid。最终 left == right 即为最小值。

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

