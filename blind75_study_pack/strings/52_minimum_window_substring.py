from typing import List, Optional, Dict, Set

# Minimum Window Substring (最小覆盖子串) - Hard
# 🔑 核心考点: 滑动窗口 / 双哈希计数表 / 双指针最优收缩
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要在 `s` 中找到包含 `t` 中所有字符的最小子串。我们可以先用滑动窗口右指针向右扩展找到一个包含所有 `t` 字符的“可行解”，然后左指针向右收缩，抛弃多余字符，直到窗口刚好不能覆盖 `t`，从而寻找局部最优解。
#   - 思维推导: 
#     1. **初始化**：用哈希表 `need` 统计 `t` 中所有字符的出现频数，`required` 为 `t` 中不重复字符的总数。哈希表 `window` 记录当前窗口内满足 `t` 所需字符的频数，变量 `have` 表示窗口中已达到 `need` 频数要求的字符数。
#     2. **滑动窗口扩张**：移动右指针 `right`，将 `s[right]` 加进 `window`：
#        - 如果 `s[right]` 在 `need` 中，且 `window[s[right]] == need[s[right]]`，说明该字符数量已达标，令 `have += 1`。
#     3. **窗口合法与收缩**：只要 `have == required`，说明窗口已完全覆盖 `t`。我们尝试收缩左侧以寻找更小的窗口：
#        - 记录当前最小长度和子串起点。
#        - 移出左侧字符 `s[left]`，更新 `window`。
#        - 如果移出的 `s[left]` 是必需的且导致频数低于 `need`，更新 `have -= 1`。
#        - 左指针向右移动 `left += 1`。
#     4. 遍历完毕后返回历史最小窗口子串，若无则返回 `""`。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        时间复杂度: O(M + N) - M 和 N 分别为字符串 s 和 t 的长度
        空间复杂度: O(M + N) - 两张哈希表占用的辅助空间
        """
        if not s or not t:
            return ""
            
        # 统计 t 中字符频数
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
            
        required = len(need)
        window = {}
        have = 0
        
        # 记录最小窗口的长度以及起点、终点索引
        res = float('inf')
        res_indices = [-1, -1]
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # 如果当前字符是所需的，且数量达到了要求
            if char in need and window[char] == need[char]:
                have += 1
                
            # 当窗口满足所有条件时，尝试收缩左指针
            while have == required:
                # 更新历史最小窗口
                if (right - left + 1) < res:
                    res = right - left + 1
                    res_indices = [left, right]
                    
                # 抛弃左边字符
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
                
        l, r = res_indices
        return s[l:r+1] if res != float('inf') else ""

