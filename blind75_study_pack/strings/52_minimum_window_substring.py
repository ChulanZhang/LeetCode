from typing import List, Optional, Dict, Set

# LeetCode 76: Minimum Window Substring - Hard
# 🔗 Link: https://leetcode.com/problems/minimum-window-substring/
# 🔑 Key Points: Sliding Window / Double Hash Maps / Optimal Shrinking
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To find the minimum window in `s` containing all characters of `t`, we can use a sliding window. We expand `right` until the window contains all characters in `t` (forming a valid window), then we shrink `left` to discard unnecessary characters, optimizing for the smallest length.
#   - Mathematical Derivation: 
#     1. **Initialization**: Create a hash map `need` to store character frequencies in `t`, and `required` representing the number of unique characters in `t` that must be matched. Use a hash map `window` for characters in the current window, and `have` representing how many unique characters have met their target frequency.
#     2. **Expansion**: Move `right` to include `s[right]` in `window`. If `s[right]` is in `need` and its frequency in `window` matches its frequency in `need`, increment `have`.
#     3. **Contraction**: While `have == required` (window is valid), we attempt to shrink the window from the left:
#        - Record the minimum window starting position and length.
#        - Remove `s[left]` from `window`.
#        - If the count of `s[left]` falls below its target in `need`, decrement `have`.
#        - Increment `left` to shift the window start.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity: O(M + N) - M and N are lengths of s and t. Each char is visited at most twice
        # Space Complexity: O(M + N) - Auxiliary space for need and window hash maps
        if not s or not t:
            return ""
            
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
            
        required = len(need)
        window = {}
        have = 0
        
        # Track minimum window length and its boundaries
        res = float('inf')
        res_indices = [-1, -1]
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # If the current character is required and its count matches the target
            if char in need and window[char] == need[char]:
                have += 1
                
            # Shrink window from the left as long as it remains valid
            while have == required:
                if (right - left + 1) < res:
                    res = right - left + 1
                    res_indices = [left, right]
                    
                # Pop left character out of the window
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
                
        l, r = res_indices
        return s[l:r+1] if res != float('inf') else ""

