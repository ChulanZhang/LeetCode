from typing import List, Optional, Dict, Set

# Merge k Sorted Lists (合并 k 个升序链表) - Hard
# 🔑 核心考点: 分治归并 (Divide and Conquer) / 最小堆 (Min-Heap)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：可以利用上一道题的“合并两个有序链表”函数。如果每次把第一条链表跟第二条合并，得到的结果再跟第三条合并... 这种朴素算法的时间复杂度是 O(N * k)，其中 N 是所有节点总数，k 是链表条数，效率较低。
#   - 思维推导: 
#     分治法（类似于归并排序）破局：
#     不需要挨个合并，我们可以采用**两两配对合并**的方式：
#     1. 假设当前有 k 个链表，我们将相邻的链表两两合并（第 0 条和第 1 条合并，第 2 条和第 3 条合并...），将 k 条链表化简为 k/2 条链表。
#     2. 重复上述合并过程，链表条数逐渐折半：k/4 -> k/8... 直到只剩下 1 条合并完成的大链表。
#     在这种两两分治合并中，合并的总层数为 $\log k$ 层。每一层中所有的节点都会参与一次合并操作，耗时为 O(N)。因此总时间复杂度被成功优化到 O(N \log k)。这种迭代的分治策略空间复杂度为 O(1)，优于使用堆（需要额外的堆空间）。

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        时间复杂度: O(N log k) - N 为所有节点总数，k 为链表总个数
        空间复杂度: O(1) - 迭代分治合并仅需常数级额外空间
        """
        if not lists:
            return None
            
        # 合并两个有序链表的辅助函数
        def merge2Lists(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next
            
        # 两两迭代归并
        interval = 1
        n = len(lists)
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]

