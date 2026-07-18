# Interval category data
PROBLEMS = {
    "35_insert_interval.py": {
        "title": "Insert Interval",
        "difficulty": "Medium",
        "key_points": "Interval Traversal & Merging - Three-Stage Partitioning",
        "analysis_intuition": "We need to insert a new interval into a list of sorted, non-overlapping intervals, ensuring the list remains sorted and non-overlapping. Directly inserting the interval and sorting the entire list ruins the pre-sorted property, taking O(N log N) time.",
        "analysis_derivation": "To solve this in linear O(N) time, we can partition the intervals into three stages during a single pass:\n1. **Before the overlap**: Add all intervals that end before the new interval starts (`interval[1] < newInterval[0]`). These can be appended to the result directly.\n2. **Overlap merging**: For any interval that overlaps with the new interval (satisfying `interval[0] <= newInterval[1]` and `interval[1] >= newInterval[0]`), merge it into the new interval by taking the minimum start time `min(interval[0], newInterval[0])` and maximum end time `max(interval[1], newInterval[1])`. This is an iterative update.\n3. **After the overlap**: Add all remaining intervals that start after the merged new interval ends (`interval[0] > newInterval[1]`).",
        "code": """from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time Complexity: O(N) - Single pass through the intervals list
        # Space Complexity: O(1) - Modifying output array directly (excluding output allocation)
        res = []
        i = 0
        n = len(intervals)
        
        # 1. Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 2. Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # 3. Add all remaining intervals that start after newInterval ends
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
"""
    },
    "36_merge_intervals.py": {
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "key_points": "Sorting + Single Pass Merging",
        "analysis_intuition": "If the intervals are unsorted, we cannot easily determine which ones overlap. By sorting the intervals by their start times, any potentially overlapping intervals will be grouped adjacent to each other.",
        "analysis_derivation": "1. Sort the intervals by their start times: `intervals.sort(key=lambda x: x[0])`.\n2. Initialize a list `merged` with the first sorted interval.\n3. For each subsequent interval `curr`:\n   - Retrieve the last merged interval `prev` from `merged`.\n   - **Overlapping condition**: If `curr[0] <= prev[1]`, the current interval starts before or at the end of the previous interval. Since the list is sorted, `curr[0] >= prev[0]` is guaranteed. We simply update the end time of `prev` to `max(prev[1], curr[1])`.\n   - **Non-overlapping condition**: If `curr[0] > prev[1]`, append `curr` as a new independent interval in `merged`.",
        "code": """from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(N log N) - Sorting dominates the time complexity; linear traversal is O(N)
        # Space Complexity: O(log N) or O(N) - Auxiliary space required by sorting algorithms
        if not intervals:
            return []
            
        # Sort intervals by their start times in ascending order
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        for curr in intervals[1:]:
            prev = merged[-1]
            # If the current interval overlaps with the previous one, merge them
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                # Otherwise, append current interval as a new entry
                merged.append(curr)
                
        return merged
"""
    },
    "37_non_overlapping_intervals.py": {
        "title": "Non-overlapping Intervals",
        "difficulty": "Medium",
        "key_points": "Greedy Algorithm - Interval Scheduling Problem",
        "analysis_intuition": "We need to remove the minimum number of intervals to eliminate all overlaps. This is mathematically equivalent to: **maximizing the number of non-overlapping intervals** we can keep. The greedy approach is optimal for this class of interval scheduling problems.",
        "analysis_derivation": "Greedy choice: To leave as much room as possible for future intervals, we should **always select the interval that ends earliest**.\n1. Sort the intervals in ascending order by their **end times**.\n2. Maintain `end` representing the end time of the last chosen interval, initialized to the first interval's end time. Maintain a `count` initialized to 0 representing removed intervals.\n3. Iterate through subsequent intervals `curr`:\n   - If `curr[0] >= end`, it starts after the previous interval ends. We can safely keep it, so we update `end = curr[1]`.\n   - If `curr[0] < end`, there is an overlap. Based on our greedy choice, we discard `curr` (since its end time is >= `end`, keeping it would only shrink future scheduling space) and increment `count` by 1.",
        "code": """from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time Complexity: O(N log N) - Sorting takes O(N log N); single pass scan takes O(N)
        # Space Complexity: O(log N) - Space complexity of the sorting algorithm
        if not intervals:
            return 0
            
        # Greedy rule: Sort intervals by end times
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        end = intervals[0][1]  # Track end time of the last scheduled interval
        
        for i in range(1, len(intervals)):
            # If current interval starts before last ended, it overlaps. Remove it.
            if intervals[i][0] < end:
                count += 1
            else:
                # Otherwise, schedule it and update the end boundary
                end = intervals[i][1]
                
        return count
"""
    },
    "38_meeting_rooms.py": {
        "title": "Meeting Rooms",
        "difficulty": "Easy",
        "key_points": "Sorting + Overlap Check",
        "analysis_intuition": "For a person to attend all meetings, there must be no overlapping intervals. We should sort the meetings chronologically and check if any adjacent meetings conflict.",
        "analysis_derivation": "1. Sort the list of meetings by their start times in ascending order.\n2. Traverse the sorted meetings, comparing adjacent meetings `i-1` and `i`:\n   - If the start time of meeting `i` is less than the end time of meeting `i-1` (`intervals[i][0] < intervals[i-1][1]`), they overlap and conflict, so we return False.\n3. If the loop completes with no conflicts, return True.",
        "code": """from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Time Complexity: O(N log N) - Sorting dominates the run time
        # Space Complexity: O(log N) - Auxiliary space required by sorting
        
        # Sort meetings by start times
        intervals.sort(key=lambda x: x[0])
        
        for i in range(1, len(intervals)):
            # If a meeting starts before the previous one ends, return False
            if intervals[i][0] < intervals[i-1][1]:
                return False
                
        return True
"""
    },
    "39_meeting_rooms_ii.py": {
        "title": "Meeting Rooms II",
        "difficulty": "Medium",
        "key_points": "Min-Heap / Two Pointers / Chronological Sweep-Line",
        "analysis_intuition": "We need to find the maximum number of concurrent meetings running at any point in time. This maximum concurrency determines the minimum number of meeting rooms required.",
        "analysis_derivation": "Chronological Sweep-Line approach:\nWe separate the start times and end times of all meetings into two distinct arrays and sort them individually.\n1. `start_times` stores all meeting start times and is sorted.\n2. `end_times` stores all meeting end times and is sorted.\n3. Place two pointers `s` and `e` at the start of these arrays. Maintain `curr_rooms` (active rooms at current timestamp) and `max_rooms` (the global peak value).\n4. Advance through time:\n   - If `start_times[s] < end_times[e]`, it means a new meeting starts before the earliest active meeting ends. We must allocate a new room: `curr_rooms += 1`, `s += 1`.\n   - If `start_times[s] >= end_times[e]`, an active meeting ends. A room is freed: `curr_rooms -= 1`, `e += 1`.\n   - At each step, update `max_rooms = max(max_rooms, curr_rooms)`. This sweep-line approach is O(N log N) and simpler than using a min-heap.",
        "code": """from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Time Complexity: O(N log N) - Sorting start and end times dominates the run time
        # Space Complexity: O(N) - Storage for start and end time arrays
        if not intervals:
            return 0
            
        # Extract and sort start times and end times independently
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        
        s, e = 0, 0
        curr_rooms = 0
        max_rooms = 0
        
        while s < len(intervals):
            # If a new meeting starts before the earliest active meeting ends
            if start_times[s] < end_times[e]:
                curr_rooms += 1
                s += 1
            else:
                # Otherwise, a meeting ended, releasing a room
                curr_rooms -= 1
                e += 1
            max_rooms = max(max_rooms, curr_rooms)
            
        return max_rooms
"""
    }
}
