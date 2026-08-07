from typing import List, Optional, Dict, Set

# LeetCode 49: Group Anagrams - Medium
# 🔗 Link: https://leetcode.com/problems/group-anagrams/
# 🔑 Key Points: Hash Map - Sorted Key Normalization
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To group anagrams together, we need to map all strings that are anagrams of each other to a single, unique 'Signature' Key in a hash map.
#   - Mathematical Derivation: 
#     Designing the Signature Key:
#     1. **Sorting**: Sort the characters of each string alphabetically. For example, 'eat', 'tea', and 'ate' all sort to 'aet'. We can use `'aet'` as the hash map key. For a string of length `L`, sorting takes $O(L \log L)$ time.
#     2. **Counting**: Map each string to a 26-tuple of character counts: `(1, 0, 0, ..., 1, ...)`. Since tuples are immutable in Python, they are hashable and can be used as keys. This takes $O(L)$ time.
#     In practice, sorting is extremely simple and fast enough for interview settings.

from typing import List

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

