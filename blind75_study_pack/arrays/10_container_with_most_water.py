from typing import List, Optional, Dict, Set

# Container With Most Water (盛最多水的容器) - Medium
# 🔑 核心考点: 双指针 (Two Pointers) / 贪心决策
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     暴力计算任意两块板组成的容器容量，复杂度为 O(N^2)。如何利用边界性质进行 O(N) 求解？
#   - 思维推导: 
#     我们使用双指针 left 和 right 分别指向数组两端。容器的宽度是 right - left，高度取决于两板中的短板 min(height[left], height[right])。每次我们将短板那一侧的指针向内移动，因为如果移动长板那一侧，容器的宽度变小了，高度依然受限于保留下的短板，面积绝对不可能增大。因此，移动短板才是唯一有可能让面积增大的贪心策略。直到两指针相遇。

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

