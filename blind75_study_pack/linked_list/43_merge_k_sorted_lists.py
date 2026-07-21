from typing import List, Optional, Dict, Set

# LeetCode 23: Merge k Sorted Lists - Hard
# 🔗 Link: https://leetcode.com/problems/merge-k-sorted-lists/
# 🔑 Key Points: Divide and Conquer / Min-Heap
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We can reuse the logic of merging two sorted lists. Merging lists sequentially (e.g., merging list 1 with list 2, then the result with list 3, and so on) has an inefficient time complexity of O(N * k), where N is the total number of nodes and k is the number of lists.
#   - Mathematical Derivation: 
#     Divide and Conquer (similar to Merge Sort):
#     Instead of merging sequentially, we merge lists in pairs:
#     1. Group the k lists into pairs and merge each pair. This reduces the number of lists from k to k/2.
#     2. Repeat this process recursively/iteratively: k/2 -> k/4 -> k/8... until only 1 merged list remains.
#     In this divide and conquer approach, the total merge height is $\log k$ levels. At each level, every node is merged once, taking O(N) time. Thus, the overall time complexity is optimized to O(N \log k). This iterative method has O(1) auxiliary space complexity, which is superior to min-heap solutions that require extra heap memory.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time Complexity: O(N log k) - N is the total number of nodes, k is the number of lists
        # Space Complexity: O(1) - Iterative divide and conquer merges in-place
        if not lists:
            return None
            
        # Helper function to merge two sorted lists
        def merge2Lists(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next
            
        # Pairwise iterative divide and conquer merge
        interval = 1
        n = len(lists)
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]

