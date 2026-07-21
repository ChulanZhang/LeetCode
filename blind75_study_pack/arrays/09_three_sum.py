from typing import List, Optional, Dict, Set

# LeetCode 15: 3Sum - Medium
# 🔗 Link: https://leetcode.com/problems/3sum/
# 🔑 Key Points: Two Pointers - Sorting
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A brute-force search of three numbers takes O(N^3) time complexity and has extremely tedious duplicate removal logic. We need an efficient way to sort, prune, and skip duplicate elements.
#   - Mathematical Derivation: 
#     1. First, sort the array in ascending order to use two pointers.
#     2. Fix the first number `nums[i]`. If `nums[i] > 0`, it's impossible to sum to 0 with subsequent positive numbers, so we break. If `nums[i] == nums[i-1]`, skip it to avoid duplicate triplets.
#     3. For the remaining range `[i + 1, n - 1]`, use two pointers `left` and `right`. If the sum is less than 0, increment `left`; if greater than 0, decrement `right`. If equal to 0, record the triplet, and shift both pointers while skipping duplicate values to prevent duplicates.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort first to enable two pointers
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break  # Pivot cannot be positive
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate pivots
                
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # Shift left and right pointers while skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

