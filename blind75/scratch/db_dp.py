# Dynamic Programming category data
PROBLEMS = {
    "16_climbing_stairs.py": {
        "title": "Climbing Stairs",
        "difficulty": "Easy",
        "key_points": "Dynamic Programming (DP) / Fibonacci Sequence",
        "analysis_intuition": "To reach the n-th step, your last step must be either a 1-step jump from the (n-1)-th step, or a 2-step jump from the (n-2)-th step. Thus, the total ways to reach the n-th step is the sum of ways to reach step n-1 and step n-2. This is the definition of the Fibonacci recurrence.",
        "analysis_derivation": "State transition equation:\n`dp[i] = dp[i-1] + dp[i-2]`\nSince calculating `dp[i]` only depends on the previous two states, we do not need to maintain a full dp array. Instead, we can use two variables `one` and `two` and scroll them forward to update, reducing the space complexity from O(N) to O(1).",
        "code": """class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity: O(n) - Single pass loop
        # Space Complexity: O(1) - Only two state variables are maintained
        if n <= 2:
            return n
            
        # 'one' represents dp[i-2], 'two' represents dp[i-1]
        one, two = 1, 2
        for _ in range(3, n + 1):
            temp = one + two
            one = two
            two = temp
            
        return two
"""
    },
    "17_coin_change.py": {
        "title": "Coin Change",
        "difficulty": "Medium",
        "key_points": "Complete Knapsack Problem / Dynamic Programming",
        "analysis_intuition": "A greedy strategy of choosing the largest denomination coin first fails for many combinations. For example, if `coins = [1, 3, 4]` and `amount = 6`, greedy selects `4 + 1 + 1` (3 coins), whereas the optimal selection is `3 + 3` (2 coins). Thus, we must evaluate all combinations using dynamic programming.",
        "analysis_derivation": "Let `dp[i]` be the minimum number of coins needed to make up amount `i`.\nTo calculate `dp[i]`, we can try taking any coin of value `coin` (where `i >= coin`). If we take that coin, the remaining amount is `i - coin`. The coin count becomes `dp[i - coin] + 1`.\nWe take the minimum over all available coins:\n`dp[i] = min(dp[i], dp[i - coin] + 1)`\nWe initialize `dp[0] = 0` and all other entries to infinity (or `amount + 1`). Finally, we check if `dp[amount]` remains at `amount + 1` (meaning it's unreachable).",
        "code": """from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity: O(n * amount) - n is the number of coin denominations
        # Space Complexity: O(amount) - DP array size is amount + 1
        
        # Initialize with amount + 1 representing infinity
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Choose minimum between not using this coin and using this coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
"""
    },
    "18_longest_increasing_subsequence.py": {
        "title": "Longest Increasing Subsequence",
        "difficulty": "Medium",
        "key_points": "Dynamic Programming O(N^2) / Binary Search with Greedy O(N log N)",
        "analysis_intuition": "Let `dp[i]` be the length of the longest increasing subsequence ending at `nums[i]`. For each element `nums[i]`, we scan all preceding elements `nums[j]` (where `j < i`). If `nums[i] > nums[j]`, we can append `nums[i]` to the subsequence ending at `nums[j]`, yielding `dp[i] = max(dp[i], dp[j] + 1)`. This takes O(N^2) time.",
        "analysis_derivation": "To achieve O(N log N) complexity, we use a greedy approach combined with binary search (Patience Sorting):\nWe maintain an array `sub`, where `sub[i]` stores the smallest tail value of all increasing subsequences of length `i+1` found so far.\nFor each number `x` in `nums`:\n- If `x` is greater than the last element of `sub`, we append `x` to `sub` (increasing the subsequence length).\n- Otherwise, we use binary search (`bisect_left`) to find the first element in `sub` that is greater than or equal to `x` and replace it with `x`. (Greedy choice: a smaller tail value makes it easier to append future elements).\nThe length of `sub` is the length of the LIS.",
        "code": """from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time Complexity: O(n log n) - Single pass through nums with a binary search in each step
        # Space Complexity: O(n) - Auxiliary array sub
        if not nums:
            return 0
            
        sub = []
        for x in nums:
            # Find the index of the first element >= x in sub
            idx = bisect.bisect_left(sub, x)
            if idx == len(sub):
                sub.append(x)  # Append if x is larger than all elements in sub
            else:
                sub[idx] = x   # Replace the element at idx with x
                
        return len(sub)
"""
    },
    "19_longest_common_subsequence.py": {
        "title": "Longest Common Subsequence",
        "difficulty": "Medium",
        "key_points": "2D Dynamic Programming (2D DP)",
        "analysis_intuition": "To find the longest common subsequence of `text1` and `text2`, we can compare characters from the ends. If they match, they can be part of the LCS. If they don't, we can try skipping the last character of either `text1` or `text2` and take the maximum.",
        "analysis_derivation": "Let `dp[i][j]` be the length of the LCS of `text1[0...i-1]` and `text2[0...j-1]`.\nState transition:\n1. If `text1[i - 1] == text2[j - 1]`, the characters match: `dp[i][j] = dp[i - 1][j - 1] + 1`.\n2. If `text1[i - 1] != text2[j - 1]`, they do not match: `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`.\nWe create a 2D matrix of size `(m+1) * (n+1)` initialized to 0. We fill the matrix bottom-up, and `dp[m][n]` yields the result.",
        "code": """class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Complexity: O(m * n) - Fill the 2D DP matrix
        # Space Complexity: O(m * n) - Size of the 2D DP matrix
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Match found: diagonal value + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match: take max of left and top values
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]
"""
    },
    "20_word_break.py": {
        "title": "Word Break",
        "difficulty": "Medium",
        "key_points": "Dynamic Programming - Substring Checking via Hash Set",
        "analysis_intuition": "A naive DFS recursively partitions `s` by matching words from `wordDict`. However, without memoization, this yields exponential time complexity due to redundant subproblem checks. We must use dynamic programming.",
        "analysis_derivation": "Let `dp[i]` be a boolean indicating whether the prefix `s[0...i-1]` can be segmented into words from `wordDict`.\nState transition:\nTo calculate `dp[i]`, we check all partitioning splits `j` (where `0 <= j < i`). If `dp[j]` is True (meaning prefix `s[0...j-1]` is valid) and the suffix `s[j...i-1]` is present in the dictionary, then `dp[i]` becomes True.\nFormula: `dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`.\nBase case: `dp[0] = True` (empty string is always valid). Output is `dp[len(s)]`.",
        "code": """from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time Complexity: O(n^2) - Outer loop n steps, inner loop checks up to n divisions
        # Space Complexity: O(n + m) - DP array size n, wordSet size m
        word_set = set(wordDict)  # O(1) average lookup time
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string is segmentable
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If prefix s[:j] is valid and suffix s[j:i] is in dict
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid partition, skip further checks for index i
                    
        return dp[len(s)]
"""
    },
    "21_combination_sum_iv.py": {
        "title": "Combination Sum IV",
        "difficulty": "Medium",
        "key_points": "Unbounded Knapsack Permutations / Dynamic Programming",
        "analysis_intuition": "This is similar to the Coin Change problem but asks for the number of combinations (permutations where different orders count as distinct). For example, if `nums = [1, 2, 3]` and `target = 4`, `(1, 3)` and `(3, 1)` are distinct. Because order matters, we iterate over the targets in the outer loop, and over the numbers in the inner loop.",
        "analysis_derivation": "Let `dp[i]` be the number of permutations that sum to `i`.\nTo make a sum of `i`, we can choose any number `num` from `nums` (where `i >= num`) as the last element. The number of permutations is then the sum of `dp[i - num]` for all choices of `num`:\n`dp[i] = sum(dp[i - num] for num in nums)`\nBase case: `dp[0] = 1` (one way to form sum 0, i.e., empty set).",
        "code": """from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(target * n) - target is the target sum, n is the size of nums
        # Space Complexity: O(target)
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to make sum 0
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]
"""
    },
    "22_house_robber.py": {
        "title": "House Robber",
        "difficulty": "Medium",
        "key_points": "Dynamic Programming - Space Optimization",
        "analysis_intuition": "When robbing houses, we cannot rob adjacent ones. At house `i`, we have two options: 1. Rob this house, meaning we cannot rob house `i-1`. The max profit is `dp[i-2] + nums[i]`. 2. Skip this house, meaning we keep the max profit from house `i-1`, which is `dp[i-1]`. We choose the maximum of these two options.",
        "analysis_derivation": "Let `dp[i]` be the max amount we can rob from the first `i` houses.\nRecurrence relation:\n`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`\nSpace Optimization: Since `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`, we can use two variables `rob1` (representing `dp[i-2]`) and `rob2` (representing `dp[i-1]`) to scroll forward, optimizing space from O(N) to O(1).",
        "code": """from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(N) - Single pass loop
        # Space Complexity: O(1) - Two variables scroll state
        
        # rob1 acts as dp[i-2], rob2 acts as dp[i-1]
        rob1, rob2 = 0, 0
        
        for num in nums:
            # Choose between robbing current house + rob1, or skipping it (rob2)
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
"""
    },
    "23_house_robber_ii.py": {
        "title": "House Robber II",
        "difficulty": "Medium",
        "key_points": "Circular Array Dynamic Programming",
        "analysis_intuition": "The only difference from House Robber I is that the houses are arranged in a circle, meaning the first house and the last house are adjacent and cannot be robbed together.",
        "analysis_derivation": "To break this circular constraint, we can split the problem into two linear subproblems:\n1. If we rob the first house, we cannot rob the last house. The problem simplifies to a linear scan of houses `[0...n-2]`.\n2. If we skip the first house, we can potentially rob the last house. The problem simplifies to a linear scan of houses `[1...n-1]`.\nSince the optimal solution must fall in one of these two categories, we run the linear solver on both sub-arrays and return the maximum of the two. Base case: if there is only 1 house, return its value directly.",
        "code": """from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(N) - Linear scans of arrays of size N-1
        # Space Complexity: O(1)
        if len(nums) == 1:
            return nums[0]
            
        # Helper to compute linear house robber
        def rob_linear(house_prices: List[int]) -> int:
            rob1, rob2 = 0, 0
            for price in house_prices:
                temp = max(rob1 + price, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        # Take the maximum of skipping the last house, and skipping the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
"""
    },
    "24_decode_ways.py": {
        "title": "Decode Ways",
        "difficulty": "Medium",
        "key_points": "Dynamic Programming - Split Checking with Leading Zeroes",
        "analysis_intuition": "We want to decode a string of digits `s` where each mapping corresponds to a character (1-26). Similar to climbing stairs, at each step we can decode either 1 digit or 2 digits, but we must validate the ranges (e.g., '0' is invalid on its own, '30' is invalid).",
        "analysis_derivation": "Let `dp[i]` be the number of decode ways for prefix `s[0...i-1]`.\nRecurrence relation:\n1. If `s[i-1]` is not `'0'`, it can be decoded as a single digit: `dp[i] += dp[i-1]`.\n2. If the two-digit substring `s[i-2:i]` forms a valid number between `'10'` and `'26'`, it can be decoded as a double digit: `dp[i] += dp[i-2]`.\nBase cases: `dp[0] = 1`. If the string starts with `'0'`, return 0. We can optimize the space to O(1) using rolling variables.",
        "code": """class Solution:
    def numDecodings(self, s: str) -> int:
        # Time Complexity: O(n) - Single pass loop
        # Space Complexity: O(1) - Two variables for state tracking
        if not s or s[0] == '0':
            return 0
            
        # prev2 acts as dp[i-2], prev1 acts as dp[i-1]
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            # 1. Decode as single digit
            if s[i] != '0':
                current += prev1
            # 2. Decode as double digit
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            prev2 = prev1
            prev1 = current
            
        return prev1
"""
    },
    "25_unique_paths.py": {
        "title": "Unique Paths",
        "difficulty": "Medium",
        "key_points": "Grid Dynamic Programming / Space Compression",
        "analysis_intuition": "Since the robot can only move down or right, any cell `(i, j)` can only be reached from the cell above `(i-1, j)` or the cell to the left `(i, j-1)`. The number of unique paths to `(i, j)` is the sum of paths to these two cells.",
        "analysis_derivation": "Let `dp[i][j]` be the number of unique paths to grid cell `(i, j)`.\nRecurrence relation:\n`dp[i][j] = dp[i-1][j] + dp[i][j-1]`\nThe first row and column are initialized to 1 because there is only one way to go straight down or right.\nSpace Optimization: Since the current row only depends on the row above and the current row's left cell, we can compress the space to a 1D array of size `n` and update it iteratively via `row[j] = row[j] + row[j-1]`.",
        "code": """class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity: O(m * n) - Single loop over all grid cells
        # Space Complexity: O(n) - Single row array to accumulate states
        
        # Initialize paths in the first row to 1
        row = [1] * n
        
        # Update row by row
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(1, n):
                # new_row[j] (left cell) + row[j] (cell from row above)
                new_row[j] = row[j] + new_row[j-1]
            row = new_row
            
        return row[n-1]
"""
    },
    "26_jump_game.py": {
        "title": "Jump Game",
        "difficulty": "Medium",
        "key_points": "Greedy Pointer Shifting",
        "analysis_intuition": "Let `dp[i]` be whether position `i` can reach the end. However, a greedy strategy traversing backwards from the goal is much more efficient and uses less space.",
        "analysis_derivation": "Greedy approach (backwards): We define our destination goal `goal` as `n-1` (the last index of the array).\nWe traverse the array from right to left. If from position `i` we can jump to or beyond the current `goal` (i.e., `i + nums[i] >= goal`), then as long as we can reach `i`, we can reach `goal`. We then shift our `goal` to `i` (`goal = i`).\nAfter checking the whole array, if `goal` successfully shifts back to `0`, we can reach the end from the start in O(N) time and O(1) space.",
        "code": """from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time Complexity: O(N) - Single pass from right to left
        # Space Complexity: O(1)
        
        # Goal is initialized to the last index of the array
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            # If current index + jump reach can hit or exceed the goal
            if i + nums[i] >= goal:
                # Update goal to be the current index
                goal = i
                
        # If goal successfully rolled back to index 0, we can reach the end
        return goal == 0
"""
    }
}
