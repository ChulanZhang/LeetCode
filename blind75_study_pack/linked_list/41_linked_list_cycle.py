from typing import List, Optional, Dict, Set

# Linked List Cycle - Easy
# 🔑 Key Points: Two Pointers - Fast & Slow Pointers (Floyd's Cycle-Finding Algorithm)
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To detect if a linked list contains a cycle, we could store visited nodes in a hash set. If we encounter a node already in the set, a cycle exists. However, this takes O(N) auxiliary space. Can we solve this in O(1) space?
#   - Mathematical Derivation: 
#     Floyd's Cycle-Finding Algorithm (Tortoise and Hare):
#     Initialize two pointers at the head:
#     - Slow pointer `slow` moves 1 step at a time: `slow = slow.next`.
#     - Fast pointer `fast` moves 2 steps at a time: `fast = fast.next.next`.
#     If the list is acyclic, `fast` will eventually reach the end of the list (null), and we can return False.
#     If the list contains a cycle, both pointers will eventually enter the loop. Since `fast` is moving twice as fast as `slow`, the relative distance between them decreases by 1 in each step. Consequently, `fast` will eventually catch up to (or lap) `slow` inside the loop (i.e., `slow == fast`), at which point we return True.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(N) - Slow pointer moves at most N steps
        # Space Complexity: O(1) - Only two pointers are allocated
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next         # Slow pointer moves 1 step
            fast = fast.next.next    # Fast pointer moves 2 steps
            
            # If pointers meet, a cycle exists
            if slow == fast:
                return True
                
        return False  # Fast pointer reached the end of the list, no cycle

