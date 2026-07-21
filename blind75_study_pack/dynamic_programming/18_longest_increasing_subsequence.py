from typing import List, Optional, Dict, Set

# LeetCode 300: Longest Increasing Subsequence - Medium
# 🔗 Link: https://leetcode.com/problems/longest-increasing-subsequence/
# 🔑 Key Points: Dynamic Programming O(N^2) / Binary Search with Greedy O(N log N)
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Let `dp[i]` be the length of the longest increasing subsequence ending at `nums[i]`. For each element `nums[i]`, we scan all preceding elements `nums[j]` (where `j < i`). If `nums[i] > nums[j]`, we can append `nums[i]` to the subsequence ending at `nums[j]`, yielding `dp[i] = max(dp[i], dp[j] + 1)`. This takes O(N^2) time.
#   - Mathematical Derivation: 
#     To achieve O(N log N) complexity, we use a greedy approach combined with binary search (Patience Sorting):
#     We maintain an array `sub`, where `sub[i]` stores the smallest tail value of all increasing subsequences of length `i+1` found so far.
#     For each number `x` in `nums`:
#     - If `x` is greater than the last element of `sub`, we append `x` to `sub` (increasing the subsequence length).
#     - Otherwise, we use binary search (`bisect_left`) to find the first element in `sub` that is greater than or equal to `x` and replace it with `x`. (Greedy choice: a smaller tail value makes it easier to append future elements).
#     The length of `sub` is the length of the LIS.

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time Complexity: O(n log n) - Single pass through nums with a binary search in each step
        # Space Complexity: O(n) - Auxiliary array sub
        if not nums:
            return 0
            
        sub = []
        for x in nums:
            # Find the index of the first element >= x in sub
            idx = bisect.bisect_left(sub, x)
            if idx == len(sub):
                sub.append(x)  # Append if x is larger than all elements in sub
            else:
                sub[idx] = x   # Replace the element at idx with x
                
        return len(sub)

