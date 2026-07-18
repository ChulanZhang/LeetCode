# Interval category data
PROBLEMS = {
    "35_insert_interval.py": {
        "title": "Insert Interval (插入区间)",
        "difficulty": "Medium",
        "key_points": "区间遍历合并 / 分段处理",
        "analysis_intuition": "直觉：我们需要在一个已经有序且互不重叠的区间列表中插入一个新区间，并确保插入后列表依然有序且无重叠。如果直接插入再排序，会打乱原本已有的有序性质，时间复杂度退化到 O(N log N)。",
        "analysis_derivation": "为了在 O(N) 的线性时间内解决问题，我们可以将原列表中的所有区间分为三部分处理：\n1. **左侧无重叠区间**：那些完全在 `newInterval` 左侧的区间（即结束时间 `interval[1] < newInterval[0]`）。这些区间直接加入结果集。\n2. **重叠区间**：那些与 `newInterval` 有交集的区间。只要区间满足 `interval[0] <= newInterval[1]` 且 `interval[1] >= newInterval[0]`，它们就与新区间重叠。我们将所有重叠的区间与新区间合并，更新区间边界为：开始时间取最小值 `min(interval[0], newInterval[0])`，结束时间取最大值 `max(interval[1], newInterval[1])`。合并是一个持续更新 `newInterval` 的过程。\n3. **右侧无重叠区间**：那些完全在合并后的新区间右侧的区间（即开始时间 `interval[0] > newInterval[1]`）。这些区间也直接加入结果集。\n这样我们仅需单次遍历数组即可搞定。",
        "code": """from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        \"\"\"
        时间复杂度: O(N) - 遍历一次区间列表
        空间复杂度: O(1) - 仅使用输出数组，无额外辅助空间
        \"\"\"
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
"""
    },
    "36_merge_intervals.py": {
        "title": "Merge Intervals (合并区间)",
        "difficulty": "Medium",
        "key_points": "排序 + 单次遍历合并",
        "analysis_intuition": "直觉：如果区间列表没有顺序，我们很难判断哪些区间存在重叠。因此，我们需要先根据区间的开始时间进行升序排序。排序后，所有可能发生合并的区间就会被排列在相邻位置。",
        "analysis_derivation": "1. 首先根据区间开始时间排序：`intervals.sort(key=lambda x: x[0])`。\n2. 初始化结果列表 `merged`，并将排序后的第一个区间放入其中。\n3. 遍历后续的每一个区间 `curr`：\n   - 取出 `merged` 列表中最后一个合并区间 `prev`。\n   - **重叠判断**：如果当前区间的开始时间小于或等于前一个区间的结束时间（即 `curr[0] <= prev[1]`），说明这两个区间重叠。由于我们排过序，`curr[0] >= prev[0]` 是必然满足的，所以只需更新前一个区间的结束时间为两者中较大值：`prev[1] = max(prev[1], curr[1])`。\n   - 如果不重叠（即 `curr[0] > prev[1]`），直接将 `curr` 作为一个新的独立区间追加到 `merged` 末尾。",
        "code": """from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        \"\"\"
        时间复杂度: O(N log N) - 排序占主导时间，后续遍历为 O(N)
        空间复杂度: O(log N) 或 O(N) - 排序算法所需的辅助空间
        \"\"\"
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
"""
    },
    "37_non_overlapping_intervals.py": {
        "title": "Non-overlapping Intervals (无重叠区间)",
        "difficulty": "Medium",
        "key_points": "贪心算法 (Greedy) - 区间调度问题 (Interval Scheduling)",
        "analysis_intuition": "直觉：我们需要移除最少数量的区间来消除所有重叠。这等价于：**保留最多数量的互不重叠的区间**。对于这类“尽可能保留更多区间”的区间调度问题，贪心策略是解决的最佳方案。",
        "analysis_derivation": "贪心策略推导：\n为了让后面能容纳更多的区间，我们在每次选择时，应该**优先选择结束时间最早的区间**（结束得越早，留给后面的空间就越大）。\n1. 将所有区间按照**结束时间**进行升序排序。\n2. 维护一个变量 `end` 记录当前已选择的最后一个区间的结束时间，初始为第一个区间的结束时间。维护计数器 `count = 0` 记录需要被移除的区间数。\n3. 遍历后续区间 `curr`：\n   - 如果 `curr[0] >= end`，说明该区间与已选区间不重叠，可以安全保留，我们更新 `end = curr[1]`。\n   - 如果 `curr[0] < end`，说明发生重叠。为了遵循贪心策略，我们应当移除这个当前区间（因为我们排过序，当前区间的结束时间一定大于或等于 `end`，保留它只会让结束时间变得更大，压榨后面的空间），计数器 `count += 1`。",
        "code": """from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        \"\"\"
        时间复杂度: O(N log N) - 排序需要 O(N log N)，单次扫描需要 O(N)
        空间复杂度: O(log N) - 排序所需的辅助空间
        \"\"\"
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
"""
    },
    "38_meeting_rooms.py": {
        "title": "Meeting Rooms (会议室)",
        "difficulty": "Easy",
        "key_points": "排序 + 重叠检测",
        "analysis_intuition": "直觉：一个人如果要能参加所有的会议，那么这些会议的召开时间不能有任何重叠。这就要求我们把会议按时间顺序排好，检查相邻的两个会议是否冲突。",
        "analysis_derivation": "1. 将会议时间列表按照每个会议的开始时间升序排序。\n2. 遍历排序后的会议，比较相邻两个会议 `i-1` 和 `i`：\n   - 如果会议 `i` 的开始时间小于会议 `i-1` 的结束时间（即 `intervals[i][0] < intervals[i-1][1]`），说明这两个会议的时间存在重叠冲突，返回 `False`。\n3. 如果全部遍历完都没有冲突，返回 `True`。",
        "code": """from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        \"\"\"
        时间复杂度: O(N log N) - 排序时间复杂度为 O(N log N)
        空间复杂度: O(log N) - 排序所需的辅助空间
        \"\"\"
        # 按会议开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            # 如果当前会议的开始时间早于上一个会议的结束时间，说明冲突了
            if intervals[i][0] < intervals[i-1][1]:
                return False
                
        return True
"""
    },
    "39_meeting_rooms_ii.py": {
        "title": "Meeting Rooms II (会议室 Ⅱ)",
        "difficulty": "Medium",
        "key_points": "堆 (Min-Heap) / 双指针 (Two Pointers) / 差分数组扫描线",
        "analysis_intuition": "直觉：我们需要计算在任何一个时间点，最多有多少个会议同时在进行。这个“最大并发数”就是我们所需要的最少会议室数量。",
        "analysis_derivation": "双指针扫描线法：\n我们将所有的会议“开始时间”和“结束时间”拆开，分别存入两个数组并单独进行升序排序。\n1. `start_times` 存储所有会议的开始时间并排序。\n2. `end_times` 存储所有会议的结束时间并排序。\n3. 使用两个指针 `s` 和 `e` 分别指向这两个数组的起点。使用 `curr_rooms` 记录当前时刻占用的房间数，`max_rooms` 记录历史最大值。\n4. 逐步推进时间：\n   - 如果 `start_times[s] < end_times[e]`，说明有一场新会议要开始，且此时还没有旧会议结束。我们需要新开一间房间：`curr_rooms += 1`, `s += 1`。\n   - 如果 `start_times[s] >= end_times[e]`，说明有会议结束了，腾出了一间会议室：`curr_rooms -= 1`, `e += 1`。\n   - 在每一步，我们用 `curr_rooms` 更新 `max_rooms = max(max_rooms, curr_rooms)`。遍历结束时 `max_rooms` 即为所求。时间复杂度为 O(N log N)，比用最小堆实现更简洁。",
        "code": """from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        \"\"\"
        时间复杂度: O(N log N) - 主要时间在两个时间数组的排序上
        空间复杂度: O(N) - 存储分离后的开始时间和结束时间数组
        \"\"\"
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
"""
    }
}
