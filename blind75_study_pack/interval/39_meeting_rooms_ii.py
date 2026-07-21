from typing import List, Optional, Dict, Set

# LeetCode 253: Meeting Rooms II - Medium
# 🔗 Link: https://leetcode.com/problems/meeting-rooms-ii/
# 🔑 Key Points: Min-Heap / Two Pointers / Chronological Sweep-Line
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to find the maximum number of concurrent meetings running at any point in time. This maximum concurrency determines the minimum number of meeting rooms required.
#   - Mathematical Derivation: 
#     Chronological Sweep-Line approach:
#     We separate the start times and end times of all meetings into two distinct arrays and sort them individually.
#     1. `start_times` stores all meeting start times and is sorted.
#     2. `end_times` stores all meeting end times and is sorted.
#     3. Place two pointers `s` and `e` at the start of these arrays. Maintain `curr_rooms` (active rooms at current timestamp) and `max_rooms` (the global peak value).
#     4. Advance through time:
#        - If `start_times[s] < end_times[e]`, it means a new meeting starts before the earliest active meeting ends. We must allocate a new room: `curr_rooms += 1`, `s += 1`.
#        - If `start_times[s] >= end_times[e]`, an active meeting ends. A room is freed: `curr_rooms -= 1`, `e += 1`.
#        - At each step, update `max_rooms = max(max_rooms, curr_rooms)`. This sweep-line approach is O(N log N) and simpler than using a min-heap.

from typing import List

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

