from typing import List, Optional, Dict, Set

# Maximum Subarray - Medium
# 🔑 Key Points: Dynamic Programming (Kadane's Algorithm)
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Brute-force checks all subarray starting and ending positions, which takes O(N^2) time complexity. If the array contains only negative numbers, initializing the maximum subarray sum to 0 is a common mistake; it must be initialized to the first element or negative infinity.
#   - Mathematical Derivation: 
#     At each position in the array, we decide whether to add the current number to the existing subarray sum, or to start a new subarray from the current number. If the previous cumulative sum is negative, it will only decrease the sum of any subsequent subarray, so we discard it and start fresh. The state transition is: `current_sum = max(num, current_sum + num)`. We track the maximum value seen during this process.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]  # Max subarray sum ending at current index
        max_sum = nums[0]      # Global max subarray sum
        
        for num in nums[1:]:
            # Choose to extend the previous subarray or start a new one
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum

