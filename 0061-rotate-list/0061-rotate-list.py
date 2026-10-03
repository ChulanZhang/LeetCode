# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head == None or head.next == None:
            return head
        
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        # make it a circle
        old_tail.next = head

        new_tail = head
        for i in range(n - k%n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head

        
        