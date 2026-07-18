from typing import List, Optional, Dict, Set

# Remove Nth Node From End of List (删除链表的倒数第 N 个节点) - Medium
# 🔑 核心考点: 双指针 - 快慢指针间距控制
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：先遍历一次链表，统计链表总长度 L，然后第二次遍历到 L-N 位置的节点，进行删除。但这需要遍历两次链表。如何做到只遍历一次？
#   - 思维推导: 
#     双指针一次遍历破局：
#     为了删除倒数第 N 个节点，我们必须能够精确定位到**该节点的前一个节点**。我们可以使用间距为 `N` 的两个指针：
#     1. 引入哑节点 `dummy` 指向 `head`（处理删除头节点的情况）。
#     2. 定义 `fast` 和 `slow` 指针均初始化为 `dummy`。
#     3. 先让 `fast` 指针前移 `N + 1` 步。此时 `fast` 和 `slow` 指针之间相差了 `N + 1` 个节点。
#     4. 然后，快慢指针以相同速度同步前进，直到 `fast` 指针指向 `None`（链表末尾的下一个位置）。
#     5. 此时，`slow` 指针正好停留在**倒数第 N 个节点的前驱节点**上。我们只需执行 `slow.next = slow.next.next` 即可完成对目标节点的删除。
#     6. 返回 `dummy.next` 作为新链表的头节点。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        时间复杂度: O(N) - 单次遍历链表
        空间复杂度: O(1)
        """
        dummy = ListNode(0, head)  # 创建哑节点，应对删除头节点的边界情况
        fast = dummy
        slow = dummy
        
        # 快指针先向前移动 n + 1 步
        for _ in range(n + 1):
            fast = fast.next
            
        # 快慢指针同步前移，直到快指针走到末尾
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 此时 slow 指向待删除节点的前驱节点，改变其指向即可删除该节点
        slow.next = slow.next.next
        
        return dummy.next

