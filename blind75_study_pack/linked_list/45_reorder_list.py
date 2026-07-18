from typing import List, Optional, Dict, Set

# Reorder List (重排链表) - Medium
# 🔑 核心考点: 快慢指针求中点 + 链表反转 + 交叉合并
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要将 `L0 -> L1 -> ... -> Ln-1 -> Ln` 重新排列为 `L0 -> Ln -> L1 -> Ln-1 -> ...`。如果直接用数组保存节点，可以容易地利用双指针从两端合并，但这需要 O(N) 的额外空间。能否做到 O(1) 额外空间？
#   - 思维推导: 
#     巧妙的链表拆分反转合并三步走：
#     我们发现，这个重排实际上是把链表的后半部分逆序之后，与前半部分交叉插入而成的。
#     1. **寻找链表的中点**：使用快慢指针，快指针每次走两步，慢指针每次走一步。当快指针到链表尾部时，慢指针所处的位置正好是前半段链表的末尾。我们将链表切分为 `first`（前半部分）和 `second`（后半部分）两段。
#     2. **反转后半部分链表**：对 `second` 链表执行就地反转操作，得到逆序后的后半部分链表。
#     3. **交叉合并**：将 `first` 和反转后的 `second` 交替连接：把 `second` 的头插在 `first` 第 1 和第 2 个节点之间，然后再移动指针。直至合并完毕。整个过程只需要修改原指针，不需要额外的节点分配。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        时间复杂度: O(N) - 找中点、反转、合并各自需要 O(N) 时间
        空间复杂度: O(1) - 原地重构链表
        """
        if not head or not head.next:
            return
            
        # 1. 快慢指针寻找中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 此时 slow 指向链表中点，将链表一分为二
        second_half = slow.next
        slow.next = None  # 断开前半段和后半段的连接
        
        # 2. 反转后半段链表
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev  # 反转后的后半段链表头节点为 prev
        
        # 3. 交叉合并两个链表
        first_half = head
        while first_half and second_half:
            # 暂存两个部分的后续节点
            tmp1 = first_half.next
            tmp2 = second_half.next
            
            # 交替链接
            first_half.next = second_half
            second_half.next = tmp1
            
            # 指针前移
            first_half = tmp1
            second_half = tmp2

