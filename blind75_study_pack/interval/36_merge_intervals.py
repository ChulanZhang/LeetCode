from typing import List, Optional, Dict, Set

# Merge Intervals (合并区间) - Medium
# 🔑 核心考点: 排序 + 单次遍历合并
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：如果区间列表没有顺序，我们很难判断哪些区间存在重叠。因此，我们需要先根据区间的开始时间进行升序排序。排序后，所有可能发生合并的区间就会被排列在相邻位置。
#   - 思维推导: 
#     1. 首先根据区间开始时间排序：`intervals.sort(key=lambda x: x[0])`。
#     2. 初始化结果列表 `merged`，并将排序后的第一个区间放入其中。
#     3. 遍历后续的每一个区间 `curr`：
#        - 取出 `merged` 列表中最后一个合并区间 `prev`。
#        - **重叠判断**：如果当前区间的开始时间小于或等于前一个区间的结束时间（即 `curr[0] <= prev[1]`），说明这两个区间重叠。由于我们排过序，`curr[0] >= prev[0]` 是必然满足的，所以只需更新前一个区间的结束时间为两者中较大值：`prev[1] = max(prev[1], curr[1])`。
#        - 如果不重叠（即 `curr[0] > prev[1]`），直接将 `curr` 作为一个新的独立区间追加到 `merged` 末尾。

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        时间复杂度: O(N log N) - 排序占主导时间，后续遍历为 O(N)
        空间复杂度: O(log N) 或 O(N) - 排序算法所需的辅助空间
        """
        if not intervals:
            return []
            
        # 按区间起点进行升序排序
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        for curr in intervals[1:]:
            # 获取已合并区间中的最后一个区间
            prev = merged[-1]
            # 如果当前区间与前一个区间重叠，更新前一个区间的结束时间
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                # 否则说明不重叠，直接作为新区间加入
                merged.append(curr)
                
        return merged

