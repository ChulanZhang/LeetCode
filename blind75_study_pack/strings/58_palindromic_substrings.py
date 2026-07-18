from typing import List, Optional, Dict, Set

# Palindromic Substrings - Medium
# 🔑 Key Points: Expand Around Center - Palindrome Counter
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to find the total count of palindromic substrings. Since every palindrome expands around a center, we can count palindromes by initiating center expansions and incrementing a counter for each successful step.
#   - Mathematical Derivation: 
#     Like the longest palindromic substring problem, we use `2N - 1` centers:
#     1. Iterate `i` from `0` to `n - 1`.
#     2. **Odd length center**: Expand from `(i, i)`. Increment `count` each time we expand successfully.
#     3. **Even length center**: Expand from `(i, i+1)`. Increment `count` each time we expand successfully.
#     4. Return the total count. This achieves O(N^2) time and O(1) space.

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time Complexity: O(N^2) - 2N - 1 centers, each can expand up to O(N) steps
        # Space Complexity: O(1)
        count = 0
        n = len(s)
        
        def expand_and_count(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        for i in range(n):
            # Check odd length palindromes centered at index i
            expand_and_count(i, i)
            # Check even length palindromes centered between i and i + 1
            expand_and_count(i, i + 1)
            
        return count

