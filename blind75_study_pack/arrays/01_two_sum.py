from typing import List, Optional, Dict, Set

# LeetCode 1: Two Sum - Easy
# 🔗 Link: https://leetcode.com/problems/two-sum/
# 🔑 Key Points: Hash Map - Space-Time Tradeoff
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The naive approach is using nested loops to check every pair of elements for a sum equal to the target, which costs O(N^2) time complexity. This is inefficient for large inputs. We need to avoid using the same element twice and handle duplicate values correctly.
#   - Mathematical Derivation: 
#     To optimize the time complexity to O(N), we can trade space for time. By traversing the array once and storing each visited element and its index in a hash map, we can check if the complement (target - current_value) exists in the hash map in O(1) average time. If it does, we return their indices.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store value-to-index mapping
        num_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement already exists in the map
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            # Store the current number with its index
            num_to_idx[num] = i
        return []

