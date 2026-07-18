from typing import List, Optional, Dict, Set

# Merge Intervals - Medium
# 🔑 Key Points: Sorting + Single Pass Merging
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     If the intervals are unsorted, we cannot easily determine which ones overlap. By sorting the intervals by their start times, any potentially overlapping intervals will be grouped adjacent to each other.
#   - Mathematical Derivation: 
#     1. Sort the intervals by their start times: `intervals.sort(key=lambda x: x[0])`.
#     2. Initialize a list `merged` with the first sorted interval.
#     3. For each subsequent interval `curr`:
#        - Retrieve the last merged interval `prev` from `merged`.
#        - **Overlapping condition**: If `curr[0] <= prev[1]`, the current interval starts before or at the end of the previous interval. Since the list is sorted, `curr[0] >= prev[0]` is guaranteed. We simply update the end time of `prev` to `max(prev[1], curr[1])`.
#        - **Non-overlapping condition**: If `curr[0] > prev[1]`, append `curr` as a new independent interval in `merged`.

from typing import List

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

