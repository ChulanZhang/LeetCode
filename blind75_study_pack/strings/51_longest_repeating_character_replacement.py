from typing import List, Optional, Dict, Set

# Longest Repeating Character Replacement - Medium
# 🔑 Key Points: Sliding Window - Dynamic Contraction & Max Freq Optimization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We want to find the longest substring that can be converted to all identical characters by replacing at most k characters. If a window has length `L` and the highest frequency of any single character in it is `max_freq`, the number of operations needed is `L - max_freq`. The window is valid if `L - max_freq <= k`.
#   - Mathematical Derivation: 
#     Using an optimized Sliding Window:
#     1. Initialize `left = 0`, a dictionary `count` to store character frequencies in the window, and a variable `max_freq = 0` to track the maximum frequency of any character seen in *any* window so far.
#     2. Iterate `right` across the string:
#        - Increment `count[s[right]]`.
#        - Update `max_freq = max(max_freq, count[s[right]])`.
#        - **Contraction check**: If the current window length minus `max_freq` exceeds `k` (i.e. `(right - left + 1) - max_freq > k`), the window is invalid. We shrink the window by decrementing `count[s[left]]` and advancing `left`.
#        - Why do we not decrement `max_freq` when shrinking the window? Because we are searching for a maximum length window. A smaller `max_freq` will only result in smaller windows, which cannot beat our historical maximum. Thus, `max_freq` only needs to be updated when it increases.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(N) - Single pass with left and right pointers
        # Space Complexity: O(1) - Dictionary size is capped at 26 uppercase English letters
        count = {}
        max_freq = 0
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            # Update max frequency found in any window so far
            max_freq = max(max_freq, count[s[right]])
            
            # If replacement operations needed exceed k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len

