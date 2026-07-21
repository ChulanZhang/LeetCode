from typing import List, Optional, Dict, Set

# LeetCode 33: Search in Rotated Sorted Array - Medium
# 🔗 Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# 🔑 Key Points: Binary Search - Split Monotonicity
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Searching for a target in a rotated sorted array. A linear scan takes O(N). We need to leverage binary search to achieve O(log N) complexity.
#   - Mathematical Derivation: 
#     A rotated sorted array has a key property: if split in half, at least one half is always strictly sorted. We can compare `nums[left]` and `nums[mid]` to determine which half is sorted:
#     1. If the left half is sorted, we check if the target lies within the range of this sorted half. If so, we search left (`right = mid - 1`), else we search right (`left = mid + 1`).
#     2. If the right half is sorted, we check if the target lies within the range of this sorted half, adjusting the binary search bounds accordingly.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is inside the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half must be sorted
            else:
                # Check if target is inside the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

