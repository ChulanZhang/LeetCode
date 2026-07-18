from typing import List, Optional, Dict, Set

# Longest Substring Without Repeating Characters (无重复字符的最长子串) - Medium
# 🔑 核心考点: 滑动窗口 (Sliding Window) / 哈希集合 (Hash Set)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要在一个字符串中找到一个最长的连续子区间，该区间内的所有字符都是唯一的。使用双重循环遍历所有子串再进行判定会耗费 O(N^2) 时间。为了将复杂度降为 O(N)，我们使用双指针滑动窗口。
#   - 思维推导: 
#     滑动窗口原理：
#     我们维护一个左指针 `left` 和右指针 `right`，定义它们之间的区间为滑动窗口。我们使用一个哈希集合 `char_set` 存储窗口内的所有字符。
#     1. `right` 逐个字符向右移动，扩张窗口。
#     2. **冲突收缩**：每当要将字符 `s[right]` 加入窗口时，如果该字符已经在 `char_set` 中，说明窗口内产生了重复字符。此时，我们必须将 `left` 指针向右移动，并同步在 `char_set` 中删除 `s[left]`，直到冲突的那个重复字符被移出窗口。
#     3. **窗口合法**：在移除冲突字符后，我们将当前的 `s[right]` 插入集合，并统计当前有效窗口的长度 `right - left + 1`，用其更新最大长度 `max_len`。
#     这样每个字符最多只被加入和移出窗口一次，时间复杂度为严格的 O(N)。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        时间复杂度: O(N) - 左右指针分别最多扫描字符串一次
        空间复杂度: O(min(M, N)) - M 为字符集的大小，N 为字符串的长度
        """
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 如果新加入的字符已存在，从左侧收缩窗口直到冲突字符被移出
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # 将当前字符加入窗口
            char_set.add(s[right])
            # 更新最大无重复子串长度
            max_len = max(max_len, right - left + 1)
            
        return max_len

