from typing import List, Optional, Dict, Set

# Reverse Linked List (反转链表) - Easy
# 🔑 核心考点: 链表基本操作 - 双指针迭代
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要反转一个单向链表，我们需要改变每个节点的指针方向，将原本指向下一个节点的指针 `next` 修改为指向它的上一个节点 `prev`。由于是单向的，改变 `next` 指向后我们会“迷失”原链表的后续路径，因此我们需要提前保存下一个节点。
#   - 思维推导: 
#     1. 声明两个指针：`curr` 指向当前节点（初始化为 `head`），`prev` 指向当前节点的前一个节点（初始化为 `None`，因为反转后的头节点指向空）。
#     2. 遍历整个链表：
#        - **保护后续节点**：用临时变量记录当前节点的下一个节点 `nxt = curr.next`。
#        - **反转指向**：把当前节点指向前一个节点 `curr.next = prev`。
#        - **双指针移动**：将 `prev` 移动到当前位置 `prev = curr`，将 `curr` 移动到保存的下一个节点位置 `curr = nxt`。
#     3. 当 `curr` 为空时，说明链表已经遍历完毕，此时 `prev` 正好指向反转后的链表头节点，返回 `prev` 即可。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度: O(N) - 遍历一次链表
        空间复杂度: O(1) - 仅使用常数个指针变量
        """
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # 暂存当前节点的下一节点，以防链表断裂
            curr.next = prev    # 反转指针方向
            prev = curr         # prev 前移
            curr = nxt          # curr 前移
            
        return prev

