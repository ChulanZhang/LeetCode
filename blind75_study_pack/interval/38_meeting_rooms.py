from typing import List, Optional, Dict, Set

# Meeting Rooms - Easy
# 🔑 Key Points: Sorting + Overlap Check
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     For a person to attend all meetings, there must be no overlapping intervals. We should sort the meetings chronologically and check if any adjacent meetings conflict.
#   - Mathematical Derivation: 
#     1. Sort the list of meetings by their start times in ascending order.
#     2. Traverse the sorted meetings, comparing adjacent meetings `i-1` and `i`:
#        - If the start time of meeting `i` is less than the end time of meeting `i-1` (`intervals[i][0] < intervals[i-1][1]`), they overlap and conflict, so we return False.
#     3. If the loop completes with no conflicts, return True.

from typing import List

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

