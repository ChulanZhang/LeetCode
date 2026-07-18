from typing import List, Optional, Dict, Set

# Word Break (单词拆分) - Medium
# 🔑 核心考点: 动态规划 / 哈希集合 (Set) 快速查找
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：使用 DFS 深度优先搜索，尝试从字符串 `s` 开头切下一个属于 `wordDict` 的单词，然后对剩余部分递归拆分。但这在遇到重叠词时容易产生重复计算，导致时间复杂度爆炸，需要记忆化或动态规划。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i]` 为字符串 `s` 的前 `i` 个字符（即子串 `s[0:i]`）是否可以被拆分为字典中的单词。
#     状态转移方程：
#     如果我们要判断 `dp[i]` 是否为真，可以枚举所有切分点 `j`（其中 `0 <= j < i`）：
#     如果 `dp[j]` 为真（即前 `j` 个字符可以被拆分），并且剩余的子串 `s[j:i]` 刚好是字典中的单词，那么 `dp[i]` 也为真。
#     公式：`dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`。
#     基础情况：`dp[0] = True`（空字符串默认可拆分）。最后返回 `dp[len(s)]`。

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        时间复杂度: O(n^2) - n 为 s 的长度，两层循环
        空间复杂度: O(n + m) - n 为 DP 数组大小，m 为字典占用的哈希集合空间
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 空串可以被拆分
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # 如果前 j 个字符可拆分，且剩余子串在字典中
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # 找到一种有效拆分方案即可
                    
        return dp[len(s)]

