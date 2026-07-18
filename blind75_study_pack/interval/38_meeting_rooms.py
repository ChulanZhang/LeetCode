from typing import List, Optional, Dict, Set

# Meeting Rooms (会议室) - Easy
# 🔑 核心考点: 排序 + 重叠检测
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：一个人如果要能参加所有的会议，那么这些会议的召开时间不能有任何重叠。这就要求我们把会议按时间顺序排好，检查相邻的两个会议是否冲突。
#   - 思维推导: 
#     1. 将会议时间列表按照每个会议的开始时间升序排序。
#     2. 遍历排序后的会议，比较相邻两个会议 `i-1` 和 `i`：
#        - 如果会议 `i` 的开始时间小于会议 `i-1` 的结束时间（即 `intervals[i][0] < intervals[i-1][1]`），说明这两个会议的时间存在重叠冲突，返回 `False`。
#     3. 如果全部遍历完都没有冲突，返回 `True`。

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        时间复杂度: O(N log N) - 排序时间复杂度为 O(N log N)
        空间复杂度: O(log N) - 排序所需的辅助空间
        """
        # 按会议开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            # 如果当前会议的开始时间早于上一个会议的结束时间，说明冲突了
            if intervals[i][0] < intervals[i-1][1]:
                return False
                
        return True

