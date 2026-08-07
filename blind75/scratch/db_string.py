# String category data
PROBLEMS = {
    "50_longest_substring_without_repeating_characters.py": {
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "key_points": "Sliding Window / Hash Set",
        "analysis_intuition": "We need to find the longest contiguous substring in which all characters are unique. A brute-force check of all substrings takes O(N^2) time. To optimize this to O(N), we can use a two-pointer sliding window.",
        "analysis_derivation": "Sliding Window Mechanism:\nWe maintain a window defined by a `left` pointer and a `right` pointer, along with a hash set `char_set` storing the unique characters inside this window.\n1. The `right` pointer moves from left to right, expanding the window and adding new characters.\n2. **Collision contraction**: If `s[right]` is already present in `char_set`, we have a duplicate. We must shrink the window from the left by removing `s[left]` from `char_set` and incrementing `left` until the duplicate character is removed from the window.\n3. **Window validity**: Once the conflict is resolved, we add `s[right]` to `char_set` and compute the current window size `right - left + 1`, updating the global maximum length `max_len`.\nEach character is added and removed from the set at most once, resulting in an O(N) time complexity.",
        "code": """class Solution:
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
"""
    },
    "51_longest_repeating_character_replacement.py": {
        "title": "Longest Repeating Character Replacement",
        "difficulty": "Medium",
        "key_points": "Sliding Window - Dynamic Contraction & Max Freq Optimization",
        "analysis_intuition": "We want to find the longest substring that can be converted to all identical characters by replacing at most k characters. If a window has length `L` and the highest frequency of any single character in it is `max_freq`, the number of operations needed is `L - max_freq`. The window is valid if `L - max_freq <= k`.",
        "analysis_derivation": "Using an optimized Sliding Window:\n1. Initialize `left = 0`, a dictionary `count` to store character frequencies in the window, and a variable `max_freq = 0` to track the maximum frequency of any character seen in *any* window so far.\n2. Iterate `right` across the string:\n   - Increment `count[s[right]]`.\n   - Update `max_freq = max(max_freq, count[s[right]])`.\n   - **Contraction check**: If the current window length minus `max_freq` exceeds `k` (i.e. `(right - left + 1) - max_freq > k`), the window is invalid. We shrink the window by decrementing `count[s[left]]` and advancing `left`.\n   - Why do we not decrement `max_freq` when shrinking the window? Because we are searching for a maximum length window. A smaller `max_freq` will only result in smaller windows, which cannot beat our historical maximum. Thus, `max_freq` only needs to be updated when it increases.",
        "code": """class Solution:
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
"""
    },
    "52_minimum_window_substring.py": {
        "title": "Minimum Window Substring",
        "difficulty": "Hard",
        "key_points": "Sliding Window / Double Hash Maps / Optimal Shrinking",
        "analysis_intuition": "To find the minimum window in `s` containing all characters of `t`, we can use a sliding window. We expand `right` until the window contains all characters in `t` (forming a valid window), then we shrink `left` to discard unnecessary characters, optimizing for the smallest length.",
        "analysis_derivation": "1. **Initialization**: Create a hash map `need` to store character frequencies in `t`, and `required` representing the number of unique characters in `t` that must be matched. Use a hash map `window` for characters in the current window, and `have` representing how many unique characters have met their target frequency.\n2. **Expansion**: Move `right` to include `s[right]` in `window`. If `s[right]` is in `need` and its frequency in `window` matches its frequency in `need`, increment `have`.\n3. **Contraction**: While `have == required` (window is valid), we attempt to shrink the window from the left:\n   - Record the minimum window starting position and length.\n   - Remove `s[left]` from `window`.\n   - If the count of `s[left]` falls below its target in `need`, decrement `have`.\n   - Increment `left` to shift the window start.",
        "code": """class Solution:
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
"""
    },
    "53_valid_anagram.py": {
        "title": "Valid Anagram",
        "difficulty": "Easy",
        "key_points": "Hash Map Frequencies / Character Counter",
        "analysis_intuition": "An anagram is a word formed by rearranging the letters of another. This means both strings must contain the exact same character frequencies.",
        "analysis_derivation": "1. Quick check: If lengths differ, they cannot be anagrams, return False.\n2. Maintain a frequency map. Loop through both strings simultaneously: increment the frequency for `s[i]` and decrement for `t[i]`.\n3. Traverse the frequency map values. If all frequencies are 0, return True; otherwise, return False.",
        "code": """class Solution:
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
"""
    },
    "54_group_anagrams.py": {
        "title": "Group Anagrams",
        "difficulty": "Medium",
        "key_points": "Hash Map - Sorted Key Normalization",
        "analysis_intuition": "To group anagrams together, we need to map all strings that are anagrams of each other to a single, unique 'Signature' Key in a hash map.",
        "analysis_derivation": "Designing the Signature Key:\n1. **Sorting**: Sort the characters of each string alphabetically. For example, 'eat', 'tea', and 'ate' all sort to 'aet'. We can use `'aet'` as the hash map key. For a string of length `L`, sorting takes $O(L \\log L)$ time.\n2. **Counting**: Map each string to a 26-tuple of character counts: `(1, 0, 0, ..., 1, ...)`. Since tuples are immutable in Python, they are hashable and can be used as keys. This takes $O(L)$ time.\nIn practice, sorting is extremely simple and fast enough for interview settings.",
        "code": """from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O(N * L log L) - N is the number of strings, L is the maximum length of a string
        # Space Complexity: O(N * L) - Space required to store the grouped strings in the map
        anagrams_map = {}
        
        for s in strs:
            # Normalize key by sorting characters alphabetically
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams_map:
                anagrams_map[sorted_s] = []
            anagrams_map[sorted_s].append(s)
            
        return list(anagrams_map.values())
"""
    },
    "55_valid_parentheses.py": {
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "key_points": "Stack Data Structure - LIFO",
        "analysis_intuition": "Parentheses matching follows a Last-In, First-Out (LIFO) pattern. The most recently opened bracket must be the first one closed. This matches the properties of a stack.",
        "analysis_derivation": "1. Initialize an empty stack `stack` and a hash map `mapping` mapping closing brackets to their corresponding opening brackets: `mapping = {')': '(', '}': '{', ']': '['}`.\n2. Traverse each character `char` in the string:\n   - If `char` is a closing bracket (in `mapping` keys):\n     - Pop the top element from the stack (or use a placeholder like `'#'` if empty). If the popped element does not match the mapped opening bracket, return False.\n   - If `char` is an opening bracket, push it onto the stack.\n3. After checking the string, return True if the stack is empty (all brackets matched), otherwise False.",
        "code": """class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(N) - Single pass traversal. Push and pop operations are O(1)
        # Space Complexity: O(N) - In the worst case (e.g. all opening brackets), stack stores all characters
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's a closing bracket, validate against the top of the stack
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto stack
                stack.append(char)
                
        # Return True only if all opening brackets have been matched and popped
        return not stack
"""
    },
    "56_valid_palindrome.py": {
        "title": "Valid Palindrome",
        "difficulty": "Easy",
        "key_points": "Two Pointers - In-Place Evaluation",
        "analysis_intuition": "We can strip out all non-alphanumeric characters, convert the remaining string to lowercase, and check if it equals its reverse. However, this takes O(N) extra space. Can we do this in-place in O(1) space?",
        "analysis_derivation": "Using two pointers on the original string:\n1. Initialize `left = 0` and `right = len(s) - 1`.\n2. While `left < right`:\n   - Skip non-alphanumeric characters on the left: `left += 1`.\n   - Skip non-alphanumeric characters on the right: `right -= 1`.\n   - Compare `s[left].lower()` with `s[right].lower()`. If they are not equal, return False.\n   - Move both pointers inward: `left += 1`, `right -= 1`.\n3. If pointers cross without mismatch, return True. This avoids any extra memory allocations.",
        "code": """class Solution:
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
"""
    },
    "57_longest_palindromic_substring.py": {
        "title": "Longest Palindromic Substring",
        "difficulty": "Medium",
        "key_points": "Expand Around Center - O(1) Space Optimization",
        "analysis_intuition": "A brute-force check of all substrings for palindromes takes O(N^3) time. Standard 2D DP takes O(N^2) time and O(N^2) space. We can optimize space to O(1) using center expansion.",
        "analysis_derivation": "Expand Around Center:\nPalindromes are symmetric around their center. We can treat each index (and gaps between indices) as a palindrome center and expand outwards:\n1. Loop `i` from `0` to `len(s) - 1`.\n2. **Odd length palindromes**: Expand from center `(i, i)` (e.g. \"aba\").\n3. **Even length palindromes**: Expand from center `(i, i+1)` (e.g. \"abba\").\n4. Expand while `left >= 0` and `right < len(s)` and `s[left] == s[right]`. Record the maximum length palindrome found.\nSince there are only `2N - 1` possible centers, the total time complexity is O(N^2) and space is O(1).",
        "code": """class Solution:
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
"""
    },
    "58_palindromic_substrings.py": {
        "title": "Palindromic Substrings",
        "difficulty": "Medium",
        "key_points": "Expand Around Center - Palindrome Counter",
        "analysis_intuition": "We need to find the total count of palindromic substrings. Since every palindrome expands around a center, we can count palindromes by initiating center expansions and incrementing a counter for each successful step.",
        "analysis_derivation": "Like the longest palindromic substring problem, we use `2N - 1` centers:\n1. Iterate `i` from `0` to `n - 1`.\n2. **Odd length center**: Expand from `(i, i)`. Increment `count` each time we expand successfully.\n3. **Even length center**: Expand from `(i, i+1)`. Increment `count` each time we expand successfully.\n4. Return the total count. This achieves O(N^2) time and O(1) space.",
        "code": """class Solution:
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
"""
    },
    "59_encode_and_decode_strings.py": {
        "title": "Encode and Decode Strings",
        "difficulty": "Medium",
        "key_points": "Serialization & Deserialization / Length-Prefixed Protocol",
        "analysis_intuition": "We need to serialize a list of strings into a single string such that it can be decoded back. Using simple delimiters (like comma or semicolon) fails if the strings themselves contain those delimiters.",
        "analysis_derivation": "Using a **Length-Prefixed Protocol** avoids delimiter collision:\n1. **Encode**: For each string `s`, we prepend its length `len(s)` followed by a non-digit delimiter (such as `'#'`), and then the string itself: `[length] + '#' + s`. For example, `[\"hello\", \"world\"]` encodes to `\"5#hello5#world\"`. If a string is `\"ab#c\"`, it encodes to `\"4#ab#c\"` without ambiguity because we know exactly how many characters to read after the delimiter.\n2. **Decode**: Maintain a pointer `i = 0` to scan the encoded string:\n   - Find the first `'#'` starting from index `i`.\n   - Read the substring before `'#'` and convert it to an integer, which is the `length` of the string.\n   - Read the next `length` characters starting immediately after `'#'` to retrieve the original string.\n   - Move the pointer to the end of the extracted string: `i = sharp_idx + 1 + length`.",
        "code": """from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        # Encodes a list of strings to a single string.
        # Time Complexity: O(N) - N is total length of all strings
        # Space Complexity: O(1) - Excluding output allocation
        res = []
        for s in strs:
            # Append length + '#' + string itself
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # Decodes a single string to a list of strings.
        # Time Complexity: O(N) - Single pass to parse the string
        # Space Complexity: O(1)
        res = []
        i = 0
        
        while i < len(s):
            # Locate the length delimiter
            sharp_idx = s.find('#', i)
            length = int(s[i:sharp_idx])
            # Slice the string according to the parsed length prefix
            start = sharp_idx + 1
            end = start + length
            res.append(s[start:end])
            # Advance pointer past the processed string segment
            i = end
            
        return res
"""
    }
}
