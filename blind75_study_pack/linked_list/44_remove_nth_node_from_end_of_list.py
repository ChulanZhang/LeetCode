from typing import List, Optional, Dict, Set

# Remove Nth Node From End of List - Medium
# 🔑 Key Points: Two Pointers - Fast & Slow Pointers Gap Control
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A naive approach is to perform a first pass to count the list length L, and a second pass to traverse to the (L-N)-th node to remove it. This requires scanning the list twice. How can we achieve this in a single pass?
#   - Mathematical Derivation: 
#     Two Pointers in a Single Pass:
#     To remove the N-th node from the end, we need to locate its **immediate predecessor**. We can maintain a gap of `N` nodes between two pointers:
#     1. Initialize a `dummy` node pointing to `head` (to handle cases where the head itself is removed).
#     2. Place `fast` and `slow` pointers at the `dummy` node.
#     3. Advance `fast` by `N + 1` steps. This establishes a gap of `N + 1` nodes between `fast` and `slow`.
#     4. Advance both pointers at the same speed until `fast` reaches null (the end of the list).
#     5. At this point, `slow` will be pointing exactly to the predecessor of the target node. We remove the target node by executing `slow.next = slow.next.next`.
#     6. Return `dummy.next`.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(N) - Single pass traversal
        # Space Complexity: O(1)
        dummy = ListNode(0, head)  # Dummy node to handle deletion of head node
        fast = dummy
        slow = dummy
        
        # Advance fast pointer by n + 1 steps to create a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers simultaneously until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # slow now points to the node preceding the target. Delete the target node.
        slow.next = slow.next.next
        
        return dummy.next

