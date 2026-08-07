from typing import List, Optional, Dict, Set

# LeetCode 5: Longest Palindromic Substring - Medium
# 🔗 Link: https://leetcode.com/problems/longest-palindromic-substring/
# 🔑 Key Points: Expand Around Center - O(1) Space Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A brute-force check of all substrings for palindromes takes O(N^3) time. Standard 2D DP takes O(N^2) time and O(N^2) space. We can optimize space to O(1) using center expansion.
#   - Mathematical Derivation: 
#     Expand Around Center:
#     Palindromes are symmetric around their center. We can treat each index (and gaps between indices) as a palindrome center and expand outwards:
#     1. Loop `i` from `0` to `len(s) - 1`.
#     2. **Odd length palindromes**: Expand from center `(i, i)` (e.g. "aba").
#     3. **Even length palindromes**: Expand from center `(i, i+1)` (e.g. "abba").
#     4. Expand while `left >= 0` and `right < len(s)` and `s[left] == s[right]`. Record the maximum length palindrome found.
#     Since there are only `2N - 1` possible centers, the total time complexity is O(N^2) and space is O(1).

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time Complexity: O(N^2) - 2N - 1 centers, each can expand up to O(N) steps
        # Space Complexity: O(1) - Only pointers and bounds are tracked
        if not s or len(s) < 1:
            return ""
            
        res = ""
        
        # Helper function to expand from center and return the palindromic substring
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            
        for i in range(len(s)):
            # Odd length center expansion
            p1 = expand(i, i)
            # Even length center expansion
            p2 = expand(i, i + 1)
            
            # Maintain the longest palindrome found
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
                
        return res

