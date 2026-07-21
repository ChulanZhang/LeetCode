from typing import List, Optional, Dict, Set

# LeetCode 55: Jump Game - Medium
# 🔗 Link: https://leetcode.com/problems/jump-game/
# 🔑 Key Points: Greedy Pointer Shifting
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Let `dp[i]` be whether position `i` can reach the end. However, a greedy strategy traversing backwards from the goal is much more efficient and uses less space.
#   - Mathematical Derivation: 
#     Greedy approach (backwards): We define our destination goal `goal` as `n-1` (the last index of the array).
#     We traverse the array from right to left. If from position `i` we can jump to or beyond the current `goal` (i.e., `i + nums[i] >= goal`), then as long as we can reach `i`, we can reach `goal`. We then shift our `goal` to `i` (`goal = i`).
#     After checking the whole array, if `goal` successfully shifts back to `0`, we can reach the end from the start in O(N) time and O(1) space.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time Complexity: O(N) - Single pass from right to left
        # Space Complexity: O(1)
        
        # Goal is initialized to the last index of the array
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            # If current index + jump reach can hit or exceed the goal
            if i + nums[i] >= goal:
                # Update goal to be the current index
                goal = i
                
        # If goal successfully rolled back to index 0, we can reach the end
        return goal == 0

