from typing import List, Optional, Dict, Set

# Jump Game (跳跃游戏) - Medium
# 🔑 核心考点: 贪心算法 (Greedy) / 动态规划状态退化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：使用动态规划，设 `dp[i]` 代表位置 `i` 能否到达终点。但由于我们只需知道“能否”，我们实际上可以从后往前思考，或者维护当前能跳到的最远边界。
#   - 思维推导: 
#     贪心思想（自后向前）：
#     我们可以维护一个目标点 `goal`，初始值为数组的最后一个索引 `n-1`（我们想去的地方）。
#     我们从右往左倒序遍历数组，如果当前位置 `i` 能够跳到或者跳过当前的 `goal`（即满足 `i + nums[i] >= goal`），说明只要我们能走到位置 `i`，就一定能走到原本的 `goal`。于是，我们可以把目标点前移更新为 `i`，即 `goal = i`。
#     当我们遍历完整个数组后，如果 `goal` 成功退回到了起点 `0`，说明我们从起点开始可以一路跳到终点。时间复杂度为 O(N)，空间复杂度为 O(1)。

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        时间复杂度: O(N) - 从后向前一次遍历
        空间复杂度: O(1)
        """
        # 初始化目标位置为数组的最后一个索引
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            # 如果当前位置加最大跳跃步数能到达或超过当前目标点
            if i + nums[i] >= goal:
                # 目标点前移到当前位置
                goal = i
                
        # 判断最终目标点是否退回到起点
        return goal == 0

