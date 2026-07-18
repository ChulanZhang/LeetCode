from typing import List, Optional, Dict, Set

# Reverse Linked List - Easy
# 🔑 Key Points: Linked List Basics - Two Pointers Iterative
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To reverse a singly linked list, we need to alter the direction of each node's pointer. Specifically, we change the `next` pointer of each node to point to its predecessor `prev`. Since it's a singly linked list, changing the `next` pointer causes us to lose the reference to the rest of the list. Thus, we must temporarily store the next node before modifying the current pointer.
#   - Mathematical Derivation: 
#     1. Initialize two pointers: `curr` pointing to the head node, and `prev` initialized to `None` (as the new tail should point to null).
#     2. Traverse the list:
#        - **Preserve successor**: Store the next node: `nxt = curr.next`.
#        - **Reverse link**: Point the current node back to the predecessor: `curr.next = prev`.
#        - **Advance pointers**: Shift `prev` to `curr` (`prev = curr`) and `curr` to the stored successor (`curr = nxt`).
#     3. When `curr` becomes null, the traversal is complete, and `prev` points to the new head of the reversed list. Return `prev`.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(N) - Single pass through the linked list
        # Space Complexity: O(1) - Constant pointer variables
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # Temporarily store the next node to prevent disconnection
            curr.next = prev    # Reverse current node's pointer
            prev = curr         # Shift prev pointer forward
            curr = nxt          # Shift curr pointer forward
            
        return prev

