class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char = set()
        longest_substring = 0

        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring

        