from typing import List, Optional, Dict, Set

# LeetCode 70: Climbing Stairs - Easy
# 🔗 Link: https://leetcode.com/problems/climbing-stairs/
# 🔑 Key Points: Dynamic Programming (DP) / Fibonacci Sequence
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To reach the n-th step, your last step must be either a 1-step jump from the (n-1)-th step, or a 2-step jump from the (n-2)-th step. Thus, the total ways to reach the n-th step is the sum of ways to reach step n-1 and step n-2. This is the definition of the Fibonacci recurrence.
#   - Mathematical Derivation: 
#     State transition equation:
#     `dp[i] = dp[i-1] + dp[i-2]`
#     Since calculating `dp[i]` only depends on the previous two states, we do not need to maintain a full dp array. Instead, we can use two variables `one` and `two` and scroll them forward to update, reducing the space complexity from O(N) to O(1).

class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity: O(n) - Single pass loop
        # Space Complexity: O(1) - Only two state variables are maintained
        if n <= 2:
            return n
            
        # 'one' represents dp[i-2], 'two' represents dp[i-1]
        one, two = 1, 2
        for _ in range(3, n + 1):
            temp = one + two
            one = two
            two = temp
            
        return two

