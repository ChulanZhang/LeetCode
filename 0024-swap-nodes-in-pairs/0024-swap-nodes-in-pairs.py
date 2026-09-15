# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dami
        dummy = ListNode(0, head)
        prev = dummy
        # we need two consecutive nodes to swap
        while prev.next and prev.next.next:
            # initialize
            first = prev.next
            second = prev.next.next

            # Before swap:
            # prev -> first -> second -> next
            # After swap:
            # prev -> second -> first -> next

            # reset connections backwards 
            first.next = second.next
            second.next = first
            prev.next = second

            # move the prev by 2 steps
            prev = first
        return dummy.next

# TC: O(n) for one pass
# SC: O(1) for dummy