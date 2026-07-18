from typing import List, Optional, Dict, Set

# Longest Common Subsequence (最长公共子序列 - LCS) - Medium
# 🔑 核心考点: 二维动态规划 (2D DP)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要在两个字符串 `text1` 和 `text2` 中寻找公共子序列。如果使用递归加记忆化的搜索方式，我们可以从两者的末尾开始匹配：如果当前字符相同，这部分可以计入公共子序列；如果不同，则分别尝试跳过其中一个字符串的末尾字符，看哪种方案得到的子序列更长。
#   - 思维推导: 
#     状态设计：
#     设 `dp[i][j]` 为 `text1` 的前 `i` 个字符和 `text2` 的前 `j` 个字符的最长公共子序列长度。
#     状态转移方程：
#     1. 如果 `text1[i - 1] == text2[j - 1]`：则当前字符匹配成功，`dp[i][j] = dp[i - 1][j - 1] + 1`。
#     2. 如果 `text1[i - 1] != text2[j - 1]`：当前字符无法匹配，我们需要决策是抛弃 `text1[i-1]` 还是抛弃 `text2[j-1]`，即：`dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`。
#     我们建立一个大小为 `(m+1) * (n+1)` 的二维 DP 矩阵，初始化为 0。自底向上填表，最终 `dp[m][n]` 就是答案。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        时间复杂度: O(m * n) - 二维网格填表
        空间复杂度: O(m * n) - DP 矩阵大小
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 字符相同，累加
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 字符不同，取跳过某一侧的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]

