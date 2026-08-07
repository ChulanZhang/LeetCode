from typing import List, Optional, Dict, Set

# LeetCode 295: Find Median from Data Stream - Hard
# 🔗 Link: https://leetcode.com/problems/find-median-from-data-stream/
# 🔑 Key Points: Dual Heaps Balance Design / Max-Heap & Min-Heap
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To find the median of a dynamic data stream, sorting on every insertion takes O(N log N) time. Using insertion sort to maintain a sorted array takes O(N) insertion time. We need a faster solution that inserts and balances in O(log N) time.
#   - Mathematical Derivation: 
#     Two Heaps (Max-Heap and Min-Heap) approach:
#     We split the numbers into two equal-sized symmetric halves:
#     - **Left half** (smaller values): Stored in a **Max-Heap `small`** (represented using negative values in Python heapq). The root represents the maximum value in the left half.
#     - **Right half** (larger values): Stored in a **Min-Heap `large`**. The root represents the minimum value in the right half.
#     To insert a new element `num`:
#     1. Push `-num` into the Max-Heap `small`.
#     2. Balance the heap boundaries: Pop the maximum element from `small` and push it to the Min-Heap `large`.
#     3. Enforce the size constraint `len(small) >= len(large)` (meaning `small` can hold at most 1 more element than `large`). If `len(large) > len(small)`, pop the minimum element from `large` and push its negative to `small`.
#     4. **Get Median**:
#        - If `len(small) > len(large)`, return the root of `small` (negated).
#        - If `len(small) == len(large)`, return `(root of small + root of large) / 2.0`.

import heapq

class MedianFinder:
    def __init__(self):
        # max-heap (values negated to simulate max-heap with heapq)
        self.small = []
        # min-heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Time Complexity: O(log N) - Heap push and pop operations
        # Push to max-heap first
        heapq.heappush(self.small, -num)
        
        # Ensure values in small (left half) are <= values in large (right half)
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # Balance heap sizes to satisfy: len(small) >= len(large)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # Time Complexity: O(1) - Root operations are constant time
        if len(self.small) > len(self.large):
            # Odd count: median is the top of the max-heap (negated)
            return float(-self.small[0])
            
        # Even count: median is the average of the two heap roots
        return (-self.small[0] + self.large[0]) / 2.0

