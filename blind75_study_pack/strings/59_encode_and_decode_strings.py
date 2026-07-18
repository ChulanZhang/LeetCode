from typing import List, Optional, Dict, Set

# Encode and Decode Strings - Medium
# 🔑 Key Points: Serialization & Deserialization / Length-Prefixed Protocol
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to serialize a list of strings into a single string such that it can be decoded back. Using simple delimiters (like comma or semicolon) fails if the strings themselves contain those delimiters.
#   - Mathematical Derivation: 
#     Using a **Length-Prefixed Protocol** avoids delimiter collision:
#     1. **Encode**: For each string `s`, we prepend its length `len(s)` followed by a non-digit delimiter (such as `'#'`), and then the string itself: `[length] + '#' + s`. For example, `["hello", "world"]` encodes to `"5#hello5#world"`. If a string is `"ab#c"`, it encodes to `"4#ab#c"` without ambiguity because we know exactly how many characters to read after the delimiter.
#     2. **Decode**: Maintain a pointer `i = 0` to scan the encoded string:
#        - Find the first `'#'` starting from index `i`.
#        - Read the substring before `'#'` and convert it to an integer, which is the `length` of the string.
#        - Read the next `length` characters starting immediately after `'#'` to retrieve the original string.
#        - Move the pointer to the end of the extracted string: `i = sharp_idx + 1 + length`.

from typing import List

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

