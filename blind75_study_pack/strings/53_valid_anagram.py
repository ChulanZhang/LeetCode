from typing import List, Optional, Dict, Set

# LeetCode 242: Valid Anagram - Easy
# 🔗 Link: https://leetcode.com/problems/valid-anagram/
# 🔑 Key Points: Hash Map Frequencies / Character Counter
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     An anagram is a word formed by rearranging the letters of another. This means both strings must contain the exact same character frequencies.
#   - Mathematical Derivation: 
#     1. Quick check: If lengths differ, they cannot be anagrams, return False.
#     2. Maintain a frequency map. Loop through both strings simultaneously: increment the frequency for `s[i]` and decrement for `t[i]`.
#     3. Traverse the frequency map values. If all frequencies are 0, return True; otherwise, return False.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity: O(N) - Single pass through both strings of length N
        # Space Complexity: O(1) - Character set is capped at 26 lowercase English letters
        if len(s) != len(t):
            return False
            
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        # If any character frequency is not balanced, return False
        for val in count.values():
            if val != 0:
                return False
                
        return True

