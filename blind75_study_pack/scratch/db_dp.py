# Dynamic Programming category data
PROBLEMS = {
    "16_climbing_stairs.py": {
        "title": "Climbing Stairs (爬楼梯)",
        "difficulty": "Easy",
        "key_points": "动态规划 (DP) / 斐波那契数列 (Fibonacci)",
        "analysis_intuition": "直觉：要爬到第 n 阶，最后一步要么是从第 n-1 阶跨了 1 步，要么是从第 n-2 阶跨了 2 步。所以，爬到第 n 阶的方法数就是爬到第 n-1 阶的方法数与爬到第 n-2 阶的方法数之和。这显然是斐波那契数列的关系。",
        "analysis_derivation": "状态转移方程：\n`dp[i] = dp[i-1] + dp[i-2]`\n由于计算 `dp[i]` 只需要前两个状态，我们不需要维持一个完整的 dp 数组，而是可以用两个变量 `one` 和 `two` 来交替滚动更新，将空间复杂度从 O(n) 降低到 O(1)。",
        "code": """class Solution:
    def climbStairs(self, n: int) -> int:
        \"\"\"
        时间复杂度: O(n) - 线性扫描一次
        空间复杂度: O(1) - 仅使用两个状态变量
        \"\"\"
        if n <= 2:
            return n
            
        # one 代表 dp[i-1]，two 代表 dp[i-2]
        one, two = 1, 2
        for _ in range(3, n + 1):
            temp = one + two
            one = two
            two = temp
            
        return two
"""
    },
    "17_coin_change.py": {
        "title": "Coin Change (零钱兑换)",
        "difficulty": "Medium",
        "key_points": "完全背包问题 / 动态规划",
        "analysis_intuition": "直觉：使用贪心策略，优先使用面值最大的硬币。但这种策略对于某些组合不成立。例如 coins = [1, 3, 4], amount = 6，贪心策略会选 4 + 1 + 1 (3枚)，但最优解是 3 + 3 (2枚)。因此必须枚举所有可能的状态，求最优解。",
        "analysis_derivation": "状态设计：\n设 `dp[i]` 为凑齐金额 `i` 所需的最少硬币数。\n状态转移方程：\n对于凑齐金额 `i`，我们可以尝试使用任何一枚硬币 `coin`。如果使用这枚硬币，剩余需要凑齐的金额就是 `i - coin`。那么此时的最少硬币数就是 `dp[i - coin] + 1`。\n我们需要在所有可用的硬币中取最小值：\n`dp[i] = min(dp[i], dp[i - coin] + 1)` 满足 `i >= coin` 且 `dp[i - coin]` 有效。\n自底向上循环计算，初始化 `dp[0] = 0`，其余设为无穷大。最后检查 `dp[amount]` 是否仍然为无穷大（代表无法凑齐）。",
        "code": """from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        \"\"\"
        时间复杂度: O(n * amount) - n 为硬币种类数，内层循环为硬币遍历
        空间复杂度: O(amount) - DP 数组大小为 amount + 1
        \"\"\"
        # 初始化为 amount + 1，相当于正无穷大（因为最多使用 amount 枚 1 元硬币）
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
"""
    },
    "18_longest_increasing_subsequence.py": {
        "title": "Longest Increasing Subsequence (最长递增子序列 - LIS)",
        "difficulty": "Medium",
        "key_points": "动态规划 O(n^2) / 二分查找搭配贪心策略 O(n log n)",
        "analysis_intuition": "直觉：使用动态规划，设 `dp[i]` 是以 `nums[i]` 结尾的最长递增子序列的长度。对于每个 `nums[i]`，遍历它前面的所有数 `nums[j]`（其中 `j < i`），如果 `nums[i] > nums[j]`，则可以把 `nums[i]` 接在以 `nums[j]` 结尾的子序列后面，状态转移为 `dp[i] = max(dp[i], dp[j] + 1)`。这需要 O(n^2) 时间复杂度。",
        "analysis_derivation": "为了达到最优的 O(n log n) 复杂度，需要结合贪心和二分查找（耐心理牌算法）：\n我们维护一个数组 `sub`，其中 `sub[i]` 存储长度为 `i+1` 的最长递增子序列的结尾元素的最小值。\n遍历 `nums` 中的每个数 `x`：\n- 如果 `x` 比 `sub` 的最后一个元素还要大，直接将 `x` 添加到 `sub` 尾部。\n- 否则，我们在 `sub` 中通过二分查找，找到第一个大于或等于 `x` 的元素，并用 `x` 替换它（贪心：越小的结尾元素，越容易在后面接上新的递增数）。\n最终 `sub` 数组的长度就是所求的最长递增子序列的长度。",
        "code": """from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        \"\"\"
        时间复杂度: O(n log n) - 遍历一次数组，每次进行一次二分查找
        空间复杂度: O(n) - 维护 sub 数组
        \"\"\"
        if not nums:
            return 0
            
        sub = []
        for x in nums:
            # 找到第一个大于或等于 x 的位置
            idx = bisect.bisect_left(sub, x)
            if idx == len(sub):
                sub.append(x)
            else:
                sub[idx] = x
                
        return len(sub)
"""
    },
    "19_longest_common_subsequence.py": {
        "title": "Longest Common Subsequence (最长公共子序列 - LCS)",
        "difficulty": "Medium",
        "key_points": "二维动态规划 (2D DP)",
        "analysis_intuition": "直觉：我们需要在两个字符串 `text1` 和 `text2` 中寻找公共子序列。如果使用递归加记忆化的搜索方式，我们可以从两者的末尾开始匹配：如果当前字符相同，这部分可以计入公共子序列；如果不同，则分别尝试跳过其中一个字符串的末尾字符，看哪种方案得到的子序列更长。",
        "analysis_derivation": "状态设计：\n设 `dp[i][j]` 为 `text1` 的前 `i` 个字符和 `text2` 的前 `j` 个字符的最长公共子序列长度。\n状态转移方程：\n1. 如果 `text1[i - 1] == text2[j - 1]`：则当前字符匹配成功，`dp[i][j] = dp[i - 1][j - 1] + 1`。\n2. 如果 `text1[i - 1] != text2[j - 1]`：当前字符无法匹配，我们需要决策是抛弃 `text1[i-1]` 还是抛弃 `text2[j-1]`，即：`dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`。\n我们建立一个大小为 `(m+1) * (n+1)` 的二维 DP 矩阵，初始化为 0。自底向上填表，最终 `dp[m][n]` 就是答案。",
        "code": """class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        \"\"\"
        时间复杂度: O(m * n) - 二维网格填表
        空间复杂度: O(m * n) - DP 矩阵大小
        \"\"\"
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
"""
    },
    "20_word_break.py": {
        "title": "Word Break (单词拆分)",
        "difficulty": "Medium",
        "key_points": "动态规划 / 哈希集合 (Set) 快速查找",
        "analysis_intuition": "直觉：使用 DFS 深度优先搜索，尝试从字符串 `s` 开头切下一个属于 `wordDict` 的单词，然后对剩余部分递归拆分。但这在遇到重叠词时容易产生重复计算，导致时间复杂度爆炸，需要记忆化或动态规划。",
        "analysis_derivation": "状态设计：\n设 `dp[i]` 为字符串 `s` 的前 `i` 个字符（即子串 `s[0:i]`）是否可以被拆分为字典中的单词。\n状态转移方程：\n如果我们要判断 `dp[i]` 是否为真，可以枚举所有切分点 `j`（其中 `0 <= j < i`）：\n如果 `dp[j]` 为真（即前 `j` 个字符可以被拆分），并且剩余的子串 `s[j:i]` 刚好是字典中的单词，那么 `dp[i]` 也为真。\n公式：`dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`。\n基础情况：`dp[0] = True`（空字符串默认可拆分）。最后返回 `dp[len(s)]`。",
        "code": """from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        \"\"\"
        时间复杂度: O(n^2) - n 为 s 的长度，两层循环
        空间复杂度: O(n + m) - n 为 DP 数组大小，m 为字典占用的哈希集合空间
        \"\"\"
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
"""
    },
    "21_combination_sum_iv.py": {
        "title": "Combination Sum IV (组合总和 Ⅳ)",
        "difficulty": "Medium",
        "key_points": "完全背包排列数 / 动态规划",
        "analysis_intuition": "直觉：本题与“零钱兑换”有些类似，但它求的是**组合的个数（实际上因为顺序不同算作不同组合，所以是排列数）**。例如 nums = [1, 2, 3], target = 4，(1, 3) 和 (3, 1) 被算作两种不同的结果。由于顺序敏感，我们在状态转移时应当将当前物品的循环放在内层。",
        "analysis_derivation": "状态设计：\n设 `dp[i]` 为组合成目标整数 `i` 的排列个数。\n状态转移方程：\n为了凑成总和 `i`，我们可以选择数组 `nums` 中的任意一个数 `num` 作为排列的最后一个数。那么在此之前我们需要凑出的总和就是 `i - num`。\n因此，凑成 `i` 的所有方法数就是所有满足 `i >= num` 的 `dp[i - num]` 之和。\n公式：\n`dp[i] = sum(dp[i - num] for num in nums)`\n基础情况：`dp[0] = 1`（凑出 0 的方法只有一种，即什么数都不选）。",
        "code": """from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        \"\"\"
        时间复杂度: O(target * n) - target 为目标和，n 为数组大小
        空间复杂度: O(target)
        \"\"\"
        dp = [0] * (target + 1)
        dp[0] = 1  # 基础状态，凑成和为 0 的排列数只有 1 种
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]
"""
    },
    "22_house_robber.py": {
        "title": "House Robber (打家劫舍)",
        "difficulty": "Medium",
        "key_points": "动态规划 - 间隔选择状态",
        "analysis_intuition": "直觉：面对一排房子，我们不能抢劫相邻的房子。在每个房子 `i` 前，我们有两个选择：1. 抢劫这间房，那么就不能抢前一间房，最大收益就是之前抢到 `i-2` 房子的最大收益加上当前房子的金额。2. 不抢这间房，那么最大收益就是抢到前一间房 `i-1` 的最大收益。我们取两者中的最大值。",
        "analysis_derivation": "状态设计：\n设 `dp[i]` 为抢劫前 `i` 间房能获得的最大金额。\n状态转移方程：\n`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`\n空间优化：由于 `dp[i]` 的计算只取决于前两步的状态，我们可以使用两个滚动变量 `rob1`（相当于 `dp[i-2]`）和 `rob2`（相当于 `dp[i-1]`），在每次遍历时交替更新它们，从而将空间复杂度从 O(N) 降低到 O(1)。",
        "code": """from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        \"\"\"
        时间复杂度: O(N) - 一次遍历
        空间复杂度: O(1) - 滚动变量优化
        \"\"\"
        # rob1 代表 dp[i-2]，rob2 代表 dp[i-1]
        rob1, rob2 = 0, 0
        
        for num in nums:
            # 决策：是抢这间房子，还是跳过这间房子
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
"""
    },
    "23_house_robber_ii.py": {
        "title": "House Robber II (打家劫舍 Ⅱ)",
        "difficulty": "Medium",
        "key_points": "环形数组动态规划",
        "analysis_intuition": "直觉：这道题和上一题的唯一区别在于房子的排列从一排变成了一个环，这意味着第一间房和最后一间房相邻，不能同时被抢。",
        "analysis_derivation": "为了破开环形依赖，我们可以把问题拆分为两个线性的子问题：\n1. 如果我们抢了第一间房，我们就绝对不能抢最后一间房。此时问题简化为在第 1 间房到第 n-1 间房中进行正常的线性抢劫规划。\n2. 如果我们不抢第一间房，我们就可以选择抢最后一间房。此时问题简化为在第 2 间房到第 n 间房中进行正常的线性抢劫规划。\n由于所有可能的最优解必然落在这两种情况之中，我们只需要对这两段子区间分别运行一次线性“打家劫舍”的求解器，并取最大值即可。注意边界情况：若只有 1 间房，直接返回其价值。",
        "code": """from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        \"\"\"
        时间复杂度: O(N) - 运行两次线性打家劫舍，均为 O(N)
        空间复杂度: O(1)
        \"\"\"
        if len(nums) == 1:
            return nums[0]
            
        # 线性打家劫舍辅助函数
        def rob_linear(house_prices: List[int]) -> int:
            rob1, rob2 = 0, 0
            for price in house_prices:
                temp = max(rob1 + price, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # 结果为：不包含最后一间房的最大值 与 不包含第一间房的最大值 中的较大者
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
"""
    },
    "24_decode_ways.py": {
        "title": "Decode Ways (解码方法)",
        "difficulty": "Medium",
        "key_points": "划分动态规划 / 边界与前导零处理",
        "analysis_intuition": "直觉：输入一个由数字组成的字符串 `s`，我们想要把它拆分成字符解码。这类似于爬楼梯问题，我们每一步可以选择解码 1 个数字，或者解码 2 个数字，但由于数字代表字符（1-26），存在有效性的限制（例如 '0' 无法单独解码，'30' 无法被解码等）。",
        "analysis_derivation": "状态设计：\n设 `dp[i]` 为字符串前 `i` 个字符构成的子串的解码方法总数。\n状态转移方程：\n1. 如果 `s[i-1]` 不为 `'0'`，那么它可以单独作为一个字符解码：`dp[i] += dp[i-1]`。\n2. 如果双位数 `s[i-2:i]` 在 `'10'` 到 `'26'` 之间，那么它可以作为两个数字的组合解码：`dp[i] += dp[i-2]`。\n初始条件：`dp[0] = 1`（空字符串有 1 种解码方式）。如果字符串以 `'0'` 开头，直接返回 0。我们可以使用滚动变量将空间优化至 O(1)。",
        "code": """class Solution:
    def numDecodings(self, s: str) -> int:
        \"\"\"
        时间复杂度: O(n) - n 为 s 的长度，遍历一次
        空间复杂度: O(1) - 滚动变量优化
        \"\"\"
        if not s or s[0] == '0':
            return 0
            
        # prev2 代表 dp[i-2]，prev1 代表 dp[i-1]
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            # 1. 尝试以单个数字解码
            if s[i] != '0':
                current += prev1
            # 2. 尝试以双位数字解码
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            prev2 = prev1
            prev1 = current
            
        return prev1
"""
    },
    "25_unique_paths.py": {
        "title": "Unique Paths (不同路径)",
        "difficulty": "Medium",
        "key_points": "网格动态规划 / 空间压缩",
        "analysis_intuition": "直觉：机器人要走到位置 `(i, j)`，因为它只能向下或向右移动，所以它只能从它的上方格 `(i-1, j)` 或者它的左侧格 `(i, j-1)` 走过来。因此，走到 `(i, j)` 的路径数就是两者之和。",
        "analysis_derivation": "状态设计：\n设 `dp[i][j]` 为走到网格 `(i, j)` 的唯一路径数。\n状态转移方程：\n`dp[i][j] = dp[i-1][j] + dp[i][j-1]`\n第一行和第一列都初始化为 1，因为只能一直向右或一直向下走。\n空间优化：由于计算当前行的状态只依赖于当前行的左侧状态和上一行的正上方状态，我们可以只维护一维数组（长度为网格宽度 `n`），不断用 `row[j] = row[j] + row[j-1]`（左侧加上正上方）来更新它，空间复杂度可以降低到 O(n)。",
        "code": """class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        \"\"\"
        时间复杂度: O(m * n) - 填充整个网格
        空间复杂度: O(n) - 维护一行状态
        \"\"\"
        # 初始第一行路径数均为 1
        row = [1] * n
        
        # 逐行更新
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(1, n):
                # new_row[j] = 上方格的值 (new_row[j]) + 左侧格的值 (new_row[j-1])
                # 注意在行滚动中，row[j] 存的就是上一行正上方格的值
                new_row[j] = row[j] + new_row[j-1]
            row = new_row
            
        return row[n-1]
"""
    },
    "26_jump_game.py": {
        "title": "Jump Game (跳跃游戏)",
        "difficulty": "Medium",
        "key_points": "贪心算法 (Greedy) / 动态规划状态退化",
        "analysis_intuition": "直觉：使用动态规划，设 `dp[i]` 代表位置 `i` 能否到达终点。但由于我们只需知道“能否”，我们实际上可以从后往前思考，或者维护当前能跳到的最远边界。",
        "analysis_derivation": "贪心思想（自后向前）：\n我们可以维护一个目标点 `goal`，初始值为数组的最后一个索引 `n-1`（我们想去的地方）。\n我们从右往左倒序遍历数组，如果当前位置 `i` 能够跳到或者跳过当前的 `goal`（即满足 `i + nums[i] >= goal`），说明只要我们能走到位置 `i`，就一定能走到原本的 `goal`。于是，我们可以把目标点前移更新为 `i`，即 `goal = i`。\n当我们遍历完整个数组后，如果 `goal` 成功退回到了起点 `0`，说明我们从起点开始可以一路跳到终点。时间复杂度为 O(N)，空间复杂度为 O(1)。",
        "code": """from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        \"\"\"
        时间复杂度: O(N) - 从后向前一次遍历
        空间复杂度: O(1)
        \"\"\"
        # 初始化目标位置为数组的最后一个索引
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            # 如果当前位置加最大跳跃步数能到达或超过当前目标点
            if i + nums[i] >= goal:
                # 目标点前移到当前位置
                goal = i
                
        # 判断最终目标点是否退回到起点
        return goal == 0
"""
    }
}
