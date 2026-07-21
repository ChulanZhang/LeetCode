from typing import List, Optional, Dict, Set

# LeetCode 268: Missing Number - Easy
# 🔗 Link: https://leetcode.com/problems/missing-number/
# 🔑 Key Points: Bit Manipulation (XOR) / Gauss Sum Formula
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Sorting the array and scanning takes O(N log N) time. Using a hash set takes O(N) time but requires O(N) auxiliary space. We need an O(N) time and O(1) space solution.
#   - Mathematical Derivation: 
#     We can solve this in O(1) space using two methods:
#     1. Gauss Sum Formula: Compute the expected sum of numbers from 0 to n using `n * (n + 1) // 2` and subtract the sum of the array. The difference is the missing number. (In languages like C++/Java, overflow must be prevented).
#     2. XOR Operation: Since `x ^ x = 0` and `x ^ 0 = x`, if we XOR all indexes `0` to `n` and all values in the array, numbers that appear twice will cancel out to 0, leaving only the missing number that appeared once. This avoids any arithmetic overflow.

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n) - Single pass through the array
        # Space Complexity: O(1)
        missing = len(nums)
        for i, num in enumerate(nums):
            # XOR indices and numbers to cancel out matches
            missing ^= i ^ num
        return missing

