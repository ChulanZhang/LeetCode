# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = l3 = ListNode(0)
        carrier = 0

        while l1 and l2:
            curr = (l1.val + l2.val + carrier) % 10
            carrier = (l1.val + l2.val + carrier) // 10
            l3.next = ListNode(curr)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        while l1:
            curr = (l1.val + carrier) % 10
            carrier = (l1.val + carrier) // 10
            l3.next = ListNode(curr)
            l1 = l1.next
            l3 = l3.next

        while l2:
            curr = (l2.val + carrier) % 10
            carrier = (l2.val + carrier) // 10
            l3.next = ListNode(curr)
            l2 = l2.next
            l3 = l3.next
        
        if carrier != 0:
            l3.next = ListNode(carrier)
        
        return dummy.next
        