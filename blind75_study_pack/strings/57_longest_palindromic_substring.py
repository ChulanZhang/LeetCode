from typing import List, Optional, Dict, Set

# Longest Palindromic Substring (最长回文子串) - Medium
# 🔑 核心考点: 中心扩散法 (Expand Around Center) / 动态规划
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：如果使用暴力枚举，找到所有可能的子串并判定是不是回文，需要 O(N^3) 的复杂度。即使使用普通的 2D 动态规划，空间和时间也均为 O(N^2)。我们需要更优的方案。
#   - 思维推导: 
#     中心扩散法（极佳的 O(1) 空间方案）推导：
#     回文串具有高度的中心对称性。我们可以尝试**以每个位置作为回文中心，向两边扩散**来寻找最长回文串：
#     1. 遍历字符串中的每一个字符索引 `i`。
#     2. **奇数长度回文**：以当前字符 `s[i]` 为中心，向两侧扩散（即左右指针初始为 `(i, i)`）。
#     3. **偶数长度回文**：以两个相邻字符 `s[i]` 和 `s[i+1]` 之间的空隙为中心，向两侧扩散（即左右指针初始为 `(i, i+1)`）。
#     4. 扩散逻辑：如果 `left >= 0` 且 `right < len(s)` 且两端字符相同 `s[left] == s[right]`，则继续扩散：`left -= 1`, `right += 1`。直到不满足条件。此时回文子串为 `s[left+1:right]`。我们统计并记录最长的回文子串。由于只有 2n-1 个可能的中心，总时间复杂度为 O(N^2)，空间为 O(1)。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        时间复杂度: O(N^2) - 每个中心扩散最多需要 O(N) 步，共有 2N-1 个中心
        空间复杂度: O(1) - 仅需存储几个指针和边界变量
        """
        if not s or len(s) < 1:
            return ""
            
        res = ""
        
        # 辅助扩散函数，返回以此为中心的最长回文子串
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            
        for i in range(len(s)):
            # 奇数长度回文 (如 "aba")
            p1 = expand(i, i)
            # 偶数长度回文 (如 "abba")
            p2 = expand(i, i + 1)
            
            # 更新全局最长回文子串
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
                
        return res

