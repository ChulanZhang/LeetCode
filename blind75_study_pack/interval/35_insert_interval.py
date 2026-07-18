from typing import List, Optional, Dict, Set

# Insert Interval (插入区间) - Medium
# 🔑 核心考点: 区间遍历合并 / 分段处理
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要在一个已经有序且互不重叠的区间列表中插入一个新区间，并确保插入后列表依然有序且无重叠。如果直接插入再排序，会打乱原本已有的有序性质，时间复杂度退化到 O(N log N)。
#   - 思维推导: 
#     为了在 O(N) 的线性时间内解决问题，我们可以将原列表中的所有区间分为三部分处理：
#     1. **左侧无重叠区间**：那些完全在 `newInterval` 左侧的区间（即结束时间 `interval[1] < newInterval[0]`）。这些区间直接加入结果集。
#     2. **重叠区间**：那些与 `newInterval` 有交集的区间。只要区间满足 `interval[0] <= newInterval[1]` 且 `interval[1] >= newInterval[0]`，它们就与新区间重叠。我们将所有重叠的区间与新区间合并，更新区间边界为：开始时间取最小值 `min(interval[0], newInterval[0])`，结束时间取最大值 `max(interval[1], newInterval[1])`。合并是一个持续更新 `newInterval` 的过程。
#     3. **右侧无重叠区间**：那些完全在合并后的新区间右侧的区间（即开始时间 `interval[0] > newInterval[1]`）。这些区间也直接加入结果集。
#     这样我们仅需单次遍历数组即可搞定。

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        时间复杂度: O(N) - 遍历一次区间列表
        空间复杂度: O(1) - 仅使用输出数组，无额外辅助空间
        """
        res = []
        i = 0
        n = len(intervals)
        
        # 1. 添加所有完全在 newInterval 左侧的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 2. 合并所有与 newInterval 重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # 3. 添加所有完全在 newInterval 右侧的区间
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res

