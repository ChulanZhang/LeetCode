from typing import List, Optional, Dict, Set

# LeetCode 11: Container With Most Water - Medium
# 🔗 Link: https://leetcode.com/problems/container-with-most-water/
# 🔑 Key Points: Two Pointers - Greedy Pointer Shifting
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Calculating the volume for every possible pair of lines takes O(N^2) time complexity. We can leverage the boundaries and solve this in O(N) using two pointers.
#   - Mathematical Derivation: 
#     We place two pointers at the two ends of the array. The width of the container is `right - left`, and the height is bounded by the shorter line `min(height[left], height[right])`. Each time, we shift the pointer pointing to the shorter line inward. Shifting the pointer pointing to the longer line cannot increase the area because the height is still capped by the shorter line, while the width decreases. Thus, moving the shorter line is the only greedy strategy that could potentially yield a larger area.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)
            # Greedily move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

