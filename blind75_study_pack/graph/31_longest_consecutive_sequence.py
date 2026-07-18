from typing import List, Optional, Dict, Set

# Longest Consecutive Sequence - Medium
# 🔑 Key Points: Hash Set - O(N) Time Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Sorting the array and scanning takes O(N log N) time complexity. We need to find an O(N) solution using extra memory.
#   - Mathematical Derivation: 
#     To achieve O(N) time complexity, we can use a hash set for O(1) membership lookups:
#     1. Insert all numbers into a hash set `num_set`.
#     2. Iterate through each number `num` in the set:
#        - Check if `num - 1` is in the set. If it is not, then `num` is the starting element of a consecutive sequence.
#        - From this starting element, increment and check for `num + 1`, `num + 2`... in the set, counting the length of this sequence.
#        - Update the global maximum length.
#     Since a sequence is only checked from its absolute starting element, each number is processed at most twice, yielding a strictly linear O(N) time complexity.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time Complexity: O(N) - Each number is processed at most twice
        # Space Complexity: O(N) - Storage for the hash set
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Check for consecutive elements
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak

