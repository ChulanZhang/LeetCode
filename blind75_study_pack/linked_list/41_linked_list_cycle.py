from typing import List, Optional, Dict, Set

# Linked List Cycle (环形链表) - Easy
# 🔑 核心考点: 双指针 - 快慢指针 (Floyd's Cycle-Finding Algorithm)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：为了检测链表是否有环，我们可以使用哈希集合 `visited` 来保存我们访问过的所有节点。如果当前节点已经存在于集合中，就说明链表有环。这需要 O(N) 的空间复杂度。是否有 $O(1)$ 空间复杂度的解法？
#   - 思维推导: 
#     快慢指针（龟兔赛跑算法）破局：
#     我们声明两个指针：
#     - 慢指针 `slow`，每次前进一步：`slow = slow.next`。
#     - 快指针 `fast`，每次前进两步：`fast = fast.next.next`。
#     如果链表没有环，快指针 `fast` 必然会率先走到链表尾部（指向 `None`），程序可以判定无环并返回 `False`。
#     如果链表有环，那么快指针和慢指针都会进入环中。由于快指针在环内的速度比慢指针快，它们之间的距离在每一轮循环中都会缩短 1 个节点。最终快指针必定会从后方“追上”慢指针（即 `slow == fast`），就像操场跑道上快跑者套圈慢跑者一样。此时判定有环，返回 `True`。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        时间复杂度: O(N) - 慢指针最多移动 N 次即可判定
        空间复杂度: O(1) - 仅使用两个辅助指针
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next         # 慢指针走一步
            fast = fast.next.next    # 快指针走两步
            
            # 如果快慢指针相遇，说明有环
            if slow == fast:
                return True
                
        return False  # 快指针到达尾部，无环

