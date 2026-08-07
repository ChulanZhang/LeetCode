from typing import List, Optional, Dict, Set

# LeetCode 3: Longest Substring Without Repeating Characters - Medium
# 🔗 Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 🔑 Key Points: Sliding Window / Hash Set
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to find the longest contiguous substring in which all characters are unique. A brute-force check of all substrings takes O(N^2) time. To optimize this to O(N), we can use a two-pointer sliding window.
#   - Mathematical Derivation: 
#     Sliding Window Mechanism:
#     We maintain a window defined by a `left` pointer and a `right` pointer, along with a hash set `char_set` storing the unique characters inside this window.
#     1. The `right` pointer moves from left to right, expanding the window and adding new characters.
#     2. **Collision contraction**: If `s[right]` is already present in `char_set`, we have a duplicate. We must shrink the window from the left by removing `s[left]` from `char_set` and incrementing `left` until the duplicate character is removed from the window.
#     3. **Window validity**: Once the conflict is resolved, we add `s[right]` to `char_set` and compute the current window size `right - left + 1`, updating the global maximum length `max_len`.
#     Each character is added and removed from the set at most once, resulting in an O(N) time complexity.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(N) - Left and right pointers scan the string at most once
        # Space Complexity: O(min(M, N)) - M is the size of the character set, N is string length
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Shrink window from the left if duplicate character is found
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the new unique character to the window
            char_set.add(s[right])
            # Update the maximum substring length seen so far
            max_len = max(max_len, right - left + 1)
            
        return max_len

