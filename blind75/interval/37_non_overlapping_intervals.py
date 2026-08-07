from typing import List, Optional, Dict, Set

# LeetCode 435: Non-overlapping Intervals - Medium
# 🔗 Link: https://leetcode.com/problems/non-overlapping-intervals/
# 🔑 Key Points: Greedy Algorithm - Interval Scheduling Problem
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We need to remove the minimum number of intervals to eliminate all overlaps. This is mathematically equivalent to: **maximizing the number of non-overlapping intervals** we can keep. The greedy approach is optimal for this class of interval scheduling problems.
#   - Mathematical Derivation: 
#     Greedy choice: To leave as much room as possible for future intervals, we should **always select the interval that ends earliest**.
#     1. Sort the intervals in ascending order by their **end times**.
#     2. Maintain `end` representing the end time of the last chosen interval, initialized to the first interval's end time. Maintain a `count` initialized to 0 representing removed intervals.
#     3. Iterate through subsequent intervals `curr`:
#        - If `curr[0] >= end`, it starts after the previous interval ends. We can safely keep it, so we update `end = curr[1]`.
#        - If `curr[0] < end`, there is an overlap. Based on our greedy choice, we discard `curr` (since its end time is >= `end`, keeping it would only shrink future scheduling space) and increment `count` by 1.

from typing import List

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

