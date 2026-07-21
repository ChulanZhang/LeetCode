from typing import List, Optional, Dict, Set

# LeetCode 217: Contains Duplicate - Easy
# 🔗 Link: https://leetcode.com/problems/contains-duplicate/
# 🔑 Key Points: Hash Set - Early Return Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A brute-force solution compares every pair of elements, resulting in O(N^2) time complexity. Using `len(set(nums)) != len(nums)` is clean but does not allow early return, which might waste memory and computation on large arrays when a duplicate is found early.
#   - Mathematical Derivation: 
#     To achieve O(N) time complexity, we can use a hash set to keep track of visited numbers. As we iterate through the array, we check if the current number is already in the set. If it is, we return True immediately (early return). Otherwise, we add it to the set. If the loop completes, it means all elements are unique.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()  # Set to track unique visited numbers
        for num in nums:
            # If the number is already visited, we found a duplicate
            if num in visited:
                return True
            visited.add(num)  # Add current number to visited set
        return False

