from typing import List, Optional, Dict, Set

# Product of Array Except Self - Medium
# 🔑 Key Points: Prefix & Suffix Products - Space Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The simplest method is to calculate the product of all elements and then divide it by each `nums[i]`. However, division is prohibited, and division by zero errors will occur if the array contains zero.
#   - Mathematical Derivation: 
#     The product of all elements except `nums[i]` can be decomposed into: the product of all elements to the left of `i` (prefix product) multiplied by the product of all elements to the right of `i` (suffix product). We can store the prefix products directly in the output array. Then, scanning backwards, we maintain a running suffix product in a variable and multiply it into the output array at each index. This achieves O(1) auxiliary space.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products and store them in the answer array
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
            
        # Calculate suffix products on the fly and multiply them into answer
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
            
        return answer

