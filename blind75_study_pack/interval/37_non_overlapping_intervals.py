from typing import List, Optional, Dict, Set

# Non-overlapping Intervals (无重叠区间) - Medium
# 🔑 核心考点: 贪心算法 (Greedy) - 区间调度问题 (Interval Scheduling)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要移除最少数量的区间来消除所有重叠。这等价于：**保留最多数量的互不重叠的区间**。对于这类“尽可能保留更多区间”的区间调度问题，贪心策略是解决的最佳方案。
#   - 思维推导: 
#     贪心策略推导：
#     为了让后面能容纳更多的区间，我们在每次选择时，应该**优先选择结束时间最早的区间**（结束得越早，留给后面的空间就越大）。
#     1. 将所有区间按照**结束时间**进行升序排序。
#     2. 维护一个变量 `end` 记录当前已选择的最后一个区间的结束时间，初始为第一个区间的结束时间。维护计数器 `count = 0` 记录需要被移除的区间数。
#     3. 遍历后续区间 `curr`：
#        - 如果 `curr[0] >= end`，说明该区间与已选区间不重叠，可以安全保留，我们更新 `end = curr[1]`。
#        - 如果 `curr[0] < end`，说明发生重叠。为了遵循贪心策略，我们应当移除这个当前区间（因为我们排过序，当前区间的结束时间一定大于或等于 `end`，保留它只会让结束时间变得更大，压榨后面的空间），计数器 `count += 1`。

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        时间复杂度: O(N log N) - 排序需要 O(N log N)，单次扫描需要 O(N)
        空间复杂度: O(log N) - 排序所需的辅助空间
        """
        if not intervals:
            return 0
            
        # 核心贪心策略：按区间结束时间进行升序排序
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # 如果当前区间起点小于上一个已保留区间的终点，说明重叠了，必须移除当前区间
            if intervals[i][0] < end:
                count += 1
            else:
                # 否则说明无重叠，更新当前保留区间的边界为当前区间终点
                end = intervals[i][1]
                
        return count

