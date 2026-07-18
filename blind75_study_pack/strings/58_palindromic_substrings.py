from typing import List, Optional, Dict, Set

# Palindromic Substrings (回文子串个数) - Medium
# 🔑 核心考点: 中心扩散法 (Expand Around Center) / 回文计数
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：这道题需要统计字符串中所有回文子串的个数。既然回文子串都是围绕某个中心对称的，我们同样可以采用中心扩散法：每成功向外扩散一步，就说明我们找到了一个新的回文子串，计数器加 1。
#   - 思维推导: 
#     与上一题“最长回文子串”类似，我们利用 2N-1 个回文中心进行扩散：
#     1. 遍历字符串中的每一个索引 `i`。
#     2. **以第 i 个字符为中心**启动扩散：
#        - 初始化 `l = i`, `r = i`。
#        - 循环检查是否满足 `l >= 0` 且 `r < len(s)` 且 `s[l] == s[r]`。只要满足，说明 `s[l:r+1]` 是回文串，计数器 `count += 1`。然后向外扩散 `l -= 1`, `r += 1`。
#     3. **以第 i 和第 i+1 个字符为中心**启动扩散：
#        - 初始化 `l = i`, `r = i + 1`。
#        - 执行同样的扩散条件和计数。
#     4. 遍历所有中心结束后，累加的总计数即为全部回文子串的数量。空间复杂度仅为 O(1)。

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        时间复杂度: O(N^2) - 每个中心最多扩散 O(N) 步
        空间复杂度: O(1)
        """
        count = 0
        n = len(s)
        
        def expand_and_count(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        for i in range(n):
            # 奇数长度中心扩散
            expand_and_count(i, i)
            # 偶数长度中心扩散
            expand_and_count(i, i + 1)
            
        return count

