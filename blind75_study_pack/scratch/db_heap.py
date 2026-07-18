# Heap category data
PROBLEMS = {
    "74_top_k_frequent_elements.py": {
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "key_points": "Hash Map Frequencies + Bucket Sort O(N) Optimal / Min-Heap O(N log K)",
        "analysis_intuition": "We can count the frequency of each element using a hash map and sort the frequencies, taking O(N log N) time. Alternatively, we can maintain a min-heap of size K containing the highest frequency elements. Pushing new elements and adjusting takes O(N log K) time.",
        "analysis_derivation": "Using Bucket Sort for an optimal O(N) solution:\nSince frequencies are bounded by `[0, N]` (where N is the array length), we can use the concept of bucket sort:\n1. Count element frequencies using a hash map.\n2. Create an array of buckets of size `N + 1`, where `buckets[i]` stores all elements that have a frequency of exactly `i`.\n3. Iterate over the frequency map, adding each element to its corresponding bucket list `buckets[freq]`.\n4. **Reverse scan**: Scan the buckets from right to left (from highest frequency `N` to lowest `0`), collecting elements until we have compiled `k` elements.\nThis avoids sorting, taking O(N) time and O(N) space, which is optimal.",
        "code": """from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(N) - Frequency counting, bucket filling, and reverse scanning take linear time
        # Space Complexity: O(N) - Auxiliary space for hash map and buckets array
        
        # 1. Count occurrences of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Create frequency buckets (index represents frequency)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Collect the top k frequent elements by scanning backwards from highest frequency
        res = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res
"""
    },
    "75_find_median_from_data_stream.py": {
        "title": "Find Median from Data Stream",
        "difficulty": "Hard",
        "key_points": "Dual Heaps Balance Design / Max-Heap & Min-Heap",
        "analysis_intuition": "To find the median of a dynamic data stream, sorting on every insertion takes O(N log N) time. Using insertion sort to maintain a sorted array takes O(N) insertion time. We need a faster solution that inserts and balances in O(log N) time.",
        "analysis_derivation": "Two Heaps (Max-Heap and Min-Heap) approach:\nWe split the numbers into two equal-sized symmetric halves:\n- **Left half** (smaller values): Stored in a **Max-Heap `small`** (represented using negative values in Python heapq). The root represents the maximum value in the left half.\n- **Right half** (larger values): Stored in a **Min-Heap `large`**. The root represents the minimum value in the right half.\nTo insert a new element `num`:\n1. Push `-num` into the Max-Heap `small`.\n2. Balance the heap boundaries: Pop the maximum element from `small` and push it to the Min-Heap `large`.\n3. Enforce the size constraint `len(small) >= len(large)` (meaning `small` can hold at most 1 more element than `large`). If `len(large) > len(small)`, pop the minimum element from `large` and push its negative to `small`.\n4. **Get Median**:\n   - If `len(small) > len(large)`, return the root of `small` (negated).\n   - If `len(small) == len(large)`, return `(root of small + root of large) / 2.0`.",
        "code": """import heapq

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
"""
    }
}
