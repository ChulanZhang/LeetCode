from typing import List, Optional, Dict, Set

# Merge Two Sorted Lists - Easy
# 🔑 Key Points: Linked List Merging / Dummy Node Technique
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To merge two sorted lists, we compare their heads and connect the smaller node to the merged list, advancing that list's pointer. This is similar to the merge step in Merge Sort.
#   - Mathematical Derivation: 
#     To avoid complex edge cases when initializing the head of the merged list, we use a **Dummy Node** `dummy`:
#     1. Initialize `dummy = ListNode(0)` and a traversal pointer `curr = dummy`.
#     2. While both `list1` and `list2` are not null:
#        - Compare `list1.val` and `list2.val`.
#        - Connect `curr.next` to the node with the smaller value, then advance that list's pointer.
#        - Advance `curr`.
#     3. Once the loop terminates, at least one list is exhausted. We append the remaining elements of the non-empty list directly to `curr.next` since they are already sorted.
#     4. Return `dummy.next`.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(N + M) - N and M are the lengths of the two lists
        # Space Complexity: O(1) - Merging is done in-place by splicing pointers
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # Append the remaining nodes of the non-empty list
        curr.next = list1 if list1 else list2
        
        return dummy.next

