from typing import List, Optional, Dict, Set

# Insert Interval - Medium
# 🔑 Key Points: Interval Traversal & Merging - Three-Stage Partitioning
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to insert a new interval into a list of sorted, non-overlapping intervals, ensuring the list remains sorted and non-overlapping. Directly inserting the interval and sorting the entire list ruins the pre-sorted property, taking O(N log N) time.
#   - Mathematical Derivation: 
#     To solve this in linear O(N) time, we can partition the intervals into three stages during a single pass:
#     1. **Before the overlap**: Add all intervals that end before the new interval starts (`interval[1] < newInterval[0]`). These can be appended to the result directly.
#     2. **Overlap merging**: For any interval that overlaps with the new interval (satisfying `interval[0] <= newInterval[1]` and `interval[1] >= newInterval[0]`), merge it into the new interval by taking the minimum start time `min(interval[0], newInterval[0])` and maximum end time `max(interval[1], newInterval[1])`. This is an iterative update.
#     3. **After the overlap**: Add all remaining intervals that start after the merged new interval ends (`interval[0] > newInterval[1]`).

from typing import List

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

