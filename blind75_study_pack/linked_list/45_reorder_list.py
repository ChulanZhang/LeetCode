from typing import List, Optional, Dict, Set

# Reorder List - Medium
# 🔑 Key Points: Find Midpoint (Fast & Slow Pointers) + Reverse List + Interleave Merge
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Reorder the list `L0 -> L1 -> ... -> Ln-1 -> Ln` to `L0 -> Ln -> L1 -> Ln-1 -> ...`. Using an auxiliary array to store nodes makes this trivial but requires O(N) extra space. We need an O(1) space solution.
#   - Mathematical Derivation: 
#     Three-Step Splicing:
#     Notice that the reordered list is formed by taking the second half of the list, reversing it, and interleaving it with the first half.
#     1. **Find midpoint**: Use fast/slow pointers. When the fast pointer reaches the end, the slow pointer points to the midpoint. Split the list into `first_half` and `second_half`.
#     2. **Reverse second half**: Reverse the `second_half` in-place.
#     3. **Interleave merge**: Interleave nodes from `first_half` and the reversed `second_half` one by one by adjusting their pointers. This requires no extra memory allocation.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Do not return anything, modify head in-place instead.
        # Time Complexity: O(N) - Finding midpoint, reversing, and merging take O(N) combined
        # Space Complexity: O(1) - Pointers modified in-place
        if not head or not head.next:
            return
            
        # 1. Find midpoint using fast/slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow points to the midpoint. Split the list.
        second_half = slow.next
        slow.next = None  # Disconnect first half from second half
        
        # 2. Reverse the second half of the list in-place
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev  # Head of the reversed second half
        
        # 3. Interleave the first half and reversed second half
        first_half = head
        while first_half and second_half:
            # Store successors
            tmp1 = first_half.next
            tmp2 = second_half.next
            
            # Interleave pointers
            first_half.next = second_half
            second_half.next = tmp1
            
            # Advance pointers
            first_half = tmp1
            second_half = tmp2

