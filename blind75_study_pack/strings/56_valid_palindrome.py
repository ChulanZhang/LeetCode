from typing import List, Optional, Dict, Set

# Valid Palindrome (验证回文串) - Easy
# 🔑 核心考点: 双指针 (Two Pointers) / 字符过滤
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：先过滤掉所有非字母和数字的字符，将所有大写字母转为小写。然后检查新字符串是否与其翻转后的字符串相同。但这需要 $O(N)$ 的额外空间。能否实现 $O(1)$ 的空间复杂度？
#   - 思维推导: 
#     双指针原地比较破局：
#     我们可以在原字符串上使用首尾双指针 `left` 和 `right`：
#     1. 初始化 `left = 0`，`right = len(s) - 1`。
#     2. 在 `left < right` 的循环中：
#        - 如果 `s[left]` 不是字母或数字，右移：`left += 1`，跳过该字符。
#        - 如果 `s[right]` 不是字母或数字，左移：`right -= 1`，跳过该字符。
#        - 如果两个指针指向的都是合法字符，转换为小写字母比对。若不相等，判定不是回文，直接返回 `False`。
#        - 若相等，双指针相向移动一步：`left += 1`，`right -= 1`。
#     3. 顺利走完循环说明是有效回文串，返回 `True`。无需分配额外空间。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        时间复杂度: O(N) - 每个字符最多被两个指针扫描一次
        空间复杂度: O(1) - 原地双指针移动，无额外开销
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # 过滤左侧非字母数字的字符
            while left < right and not s[left].isalnum():
                left += 1
            # 过滤右侧非字母数字的字符
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 比较是否相等（忽略大小写）
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True

