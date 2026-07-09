# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle → reverse second half → merge two halves
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # break the original linked-list into two parts
        second = slow.next
        slow.next = None

        # reverse the second half
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge the two parts
        second = prev
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        


        