from typing import List, Optional, Dict, Set

# Valid Anagram (有效的字母异位词) - Easy
# 🔑 核心考点: 哈希计数表 / 字符统计
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：字母异位词指的是两个字符串所包含的字母及其出现的频数完全相同，只是顺序不同。我们可以直接统计两个字符串的字符个数进行比对。
#   - 思维推导: 
#     1. 快速检查：如果两个字符串的长度不相等，直接返回 `False`。
#     2. 使用一个哈希计数表，遍历 `s` 的每个字符令频数加 1，遍历 `t` 的每个字符令频数减 1。
#     3. 最后遍历哈希表，如果所有字符的频数都为 0，说明它是合法的异位词，返回 `True`；否则返回 `False`。或者直接使用 Python 的 `collections.Counter` 对比，其底层同样是这一原理。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        时间复杂度: O(N) - 一次遍历统计字符频数
        空间复杂度: O(1) - 字符集为 26 个小写字母，哈希表大小最多为 26，为常数空间
        """
        if len(s) != len(t):
            return False
            
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        for val in count.values():
            if val != 0:
                return False
                
        return True

