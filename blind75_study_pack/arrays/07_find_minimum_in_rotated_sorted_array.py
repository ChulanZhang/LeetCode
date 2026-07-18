from typing import List, Optional, Dict, Set

# Find Minimum in Rotated Sorted Array - Medium
# 🔑 Key Points: Binary Search
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Finding the minimum in a rotated sorted array. A linear scan takes O(N). Because the array was originally sorted, we must solve it in O(log N) time using binary search.
#   - Mathematical Derivation: 
#     Using binary search, if the middle value `nums[mid]` is greater than the right boundary `nums[right]`, it means the rotation inflection point lies to the right of `mid`, so the minimum must be in the range `[mid + 1, right]`. Otherwise, the right half is sorted, and the minimum is either `nums[mid]` or lies to the left of `mid`. Thus, we update `right = mid`. We repeat this until `left == right`.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Inflection point must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            # Inflection point is at mid or to the left of mid
            else:
                right = mid
        return nums[left]

