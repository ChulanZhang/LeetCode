from typing import List, Optional, Dict, Set

# Meeting Rooms II (会议室 Ⅱ) - Medium
# 🔑 核心考点: 堆 (Min-Heap) / 双指针 (Two Pointers) / 差分数组扫描线
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要计算在任何一个时间点，最多有多少个会议同时在进行。这个“最大并发数”就是我们所需要的最少会议室数量。
#   - 思维推导: 
#     双指针扫描线法：
#     我们将所有的会议“开始时间”和“结束时间”拆开，分别存入两个数组并单独进行升序排序。
#     1. `start_times` 存储所有会议的开始时间并排序。
#     2. `end_times` 存储所有会议的结束时间并排序。
#     3. 使用两个指针 `s` 和 `e` 分别指向这两个数组的起点。使用 `curr_rooms` 记录当前时刻占用的房间数，`max_rooms` 记录历史最大值。
#     4. 逐步推进时间：
#        - 如果 `start_times[s] < end_times[e]`，说明有一场新会议要开始，且此时还没有旧会议结束。我们需要新开一间房间：`curr_rooms += 1`, `s += 1`。
#        - 如果 `start_times[s] >= end_times[e]`，说明有会议结束了，腾出了一间会议室：`curr_rooms -= 1`, `e += 1`。
#        - 在每一步，我们用 `curr_rooms` 更新 `max_rooms = max(max_rooms, curr_rooms)`。遍历结束时 `max_rooms` 即为所求。时间复杂度为 O(N log N)，比用最小堆实现更简洁。

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        时间复杂度: O(N log N) - 主要时间在两个时间数组的排序上
        空间复杂度: O(N) - 存储分离后的开始时间和结束时间数组
        """
        if not intervals:
            return 0
            
        # 分离开始和结束时间并排序
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        
        s, e = 0, 0
        curr_rooms = 0
        max_rooms = 0
        
        while s < len(intervals):
            # 如果有新会议开始，且在当前最早会议结束之前
            if start_times[s] < end_times[e]:
                curr_rooms += 1
                s += 1
            else:
                # 否则，说明有会议结束了，释放一间会议室
                curr_rooms -= 1
                e += 1
            max_rooms = max(max_rooms, curr_rooms)
            
        return max_rooms

