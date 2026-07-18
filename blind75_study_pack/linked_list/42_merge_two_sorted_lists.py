from typing import List, Optional, Dict, Set

# Merge Two Sorted Lists (合并两个有序链表) - Easy
# 🔑 核心考点: 链表合并 / 哑节点 (Dummy Node) 技巧
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要合并两个递增链表，类似于归并排序中的 merge 过程。我们比较两个链表的头节点，取较小的节点连接到新链表上，然后移动指针。
#   - 思维推导: 
#     为了避免在初始化新链表头部时进行大量的空指针（null）特殊判断，我们引入一个**哑节点 (Dummy Node)** `dummy`。
#     1. 初始化哑节点 `dummy = ListNode(0)`，定义一个指针 `curr` 指向它。
#     2. 在 `list1` 和 `list2` 都不为空的循环中，比对两者的值：
#        - 如果 `list1.val <= list2.val`，则将 `curr.next` 连向 `list1`，并将 `list1` 前移。
#        - 否则，将 `curr.next` 连向 `list2`，并将 `list2` 前移。
#        - 接着把新链表的遍历指针 `curr` 前移。
#     3. 当循环退出时，必然有一个链表已经处理完毕。我们直接将未处理完的那部分链表接到 `curr.next` 后面（因为有序，无需继续逐个比对）。
#     4. 返回 `dummy.next`，即为合并后有序链表的实际头部。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        时间复杂度: O(N + M) - N 和 M 分别为两条链表的长度
        空间复杂度: O(1) - 原地拼接指针，无额外分配空间
        """
        dummy = ListNode(0)  # 哑节点，简化首节点处理逻辑
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # 拼接剩余未遍历完的链表部分
        curr.next = list1 if list1 else list2
        
        return dummy.next

