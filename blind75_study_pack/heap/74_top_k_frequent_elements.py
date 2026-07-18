from typing import List, Optional, Dict, Set

# Top K Frequent Elements - Medium
# 🔑 Key Points: Hash Map Frequencies + Bucket Sort O(N) Optimal / Min-Heap O(N log K)
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We can count the frequency of each element using a hash map and sort the frequencies, taking O(N log N) time. Alternatively, we can maintain a min-heap of size K containing the highest frequency elements. Pushing new elements and adjusting takes O(N log K) time.
#   - Mathematical Derivation: 
#     Using Bucket Sort for an optimal O(N) solution:
#     Since frequencies are bounded by `[0, N]` (where N is the array length), we can use the concept of bucket sort:
#     1. Count element frequencies using a hash map.
#     2. Create an array of buckets of size `N + 1`, where `buckets[i]` stores all elements that have a frequency of exactly `i`.
#     3. Iterate over the frequency map, adding each element to its corresponding bucket list `buckets[freq]`.
#     4. **Reverse scan**: Scan the buckets from right to left (from highest frequency `N` to lowest `0`), collecting elements until we have compiled `k` elements.
#     This avoids sorting, taking O(N) time and O(N) space, which is optimal.

from typing import List

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

