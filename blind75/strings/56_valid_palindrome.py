from typing import List, Optional, Dict, Set

# LeetCode 125: Valid Palindrome - Easy
# 🔗 Link: https://leetcode.com/problems/valid-palindrome/
# 🔑 Key Points: Two Pointers - In-Place Evaluation
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We can strip out all non-alphanumeric characters, convert the remaining string to lowercase, and check if it equals its reverse. However, this takes O(N) extra space. Can we do this in-place in O(1) space?
#   - Mathematical Derivation: 
#     Using two pointers on the original string:
#     1. Initialize `left = 0` and `right = len(s) - 1`.
#     2. While `left < right`:
#        - Skip non-alphanumeric characters on the left: `left += 1`.
#        - Skip non-alphanumeric characters on the right: `right -= 1`.
#        - Compare `s[left].lower()` with `s[right].lower()`. If they are not equal, return False.
#        - Move both pointers inward: `left += 1`, `right -= 1`.
#     3. If pointers cross without mismatch, return True. This avoids any extra memory allocations.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time Complexity: O(N) - In the worst case, pointers scan the string once
        # Space Complexity: O(1) - Constant auxiliary space
        left, right = 0, len(s) - 1
        
        while left < right:
            # Advance left pointer if current character is non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Decrement right pointer if current character is non-alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Case-insensitive comparison
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True

