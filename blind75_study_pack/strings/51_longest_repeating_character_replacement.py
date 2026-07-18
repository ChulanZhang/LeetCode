from typing import List, Optional, Dict, Set

# Longest Repeating Character Replacement (替换后的最长重复字符) - Medium
# 🔑 核心考点: 滑动窗口 / 双指针 / 局部频数统计优化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们要找一个最长子串，该子串通过替换不超过 k 个字符后可以全部变成同一个字符。如果窗口大小为 `L`，且窗口中出现频率最高的字符次数为 `max_freq`，那么要让这个窗口内字符全部相同，需要替换的字符数就是 `L - max_freq`。只要 `L - max_freq <= k`，这个窗口就是可行的。
#   - 思维推导: 
#     使用滑动窗口进行优化：
#     1. 初始化 `left = 0`，最大频率记录 `max_freq = 0`，以及一个记录窗口内字符频数的哈希表/数组 `count`。
#     2. 遍历右指针 `right`：
#        - 更新当前字符 `s[right]` 的频数：`count[s[right]] += 1`。
#        - 更新窗口内的最大字符频数：`max_freq = max(max_freq, count[s[right]])`。
#        - **收缩条件**：如果当前窗口长度减去最大频数大于 k（即 `(right - left + 1) - max_freq > k`），说明即使把所有非最频字符都替换掉，也无法在 k 次内达到全部相同。此时我们必须收缩窗口：将 `left` 对应字符频数减 1，并向右移动 `left` 指针。
#        - 为什么不需要在收缩窗口时重新计算真正的 `max_freq` 最小值？因为我们只想找更长的子串。当窗口变小时，`max_freq` 的变小不会帮助我们找到比目前历史记录更大的最长子串，所以我们在收缩时保持 `max_freq` 不变也是正确且安全的。
#     3. 记录窗口历史最大长度并返回。

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        时间复杂度: O(N) - N 为字符串的长度，每个字符最多被扫描两次
        空间复杂度: O(1) - 仅需大小为 26 的频数哈希表/数组
        """
        count = {}
        max_freq = 0
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 累加当前字符频数
            count[s[right]] = count.get(s[right], 0) + 1
            # 维护窗口内的历史最大频数
            max_freq = max(max_freq, count[s[right]])
            
            # 如果需要替换的字符个数超过 k，收缩左指针
            # 窗口宽度为 right - left + 1
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len

