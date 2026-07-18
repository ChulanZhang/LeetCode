# Linked List category data
PROBLEMS = {
    "40_reverse_linked_list.py": {
        "title": "Reverse Linked List (反转链表)",
        "difficulty": "Easy",
        "key_points": "链表基本操作 - 双指针迭代",
        "analysis_intuition": "直觉：要反转一个单向链表，我们需要改变每个节点的指针方向，将原本指向下一个节点的指针 `next` 修改为指向它的上一个节点 `prev`。由于是单向的，改变 `next` 指向后我们会“迷失”原链表的后续路径，因此我们需要提前保存下一个节点。",
        "analysis_derivation": "1. 声明两个指针：`curr` 指向当前节点（初始化为 `head`），`prev` 指向当前节点的前一个节点（初始化为 `None`，因为反转后的头节点指向空）。\n2. 遍历整个链表：\n   - **保护后续节点**：用临时变量记录当前节点的下一个节点 `nxt = curr.next`。\n   - **反转指向**：把当前节点指向前一个节点 `curr.next = prev`。\n   - **双指针移动**：将 `prev` 移动到当前位置 `prev = curr`，将 `curr` 移动到保存的下一个节点位置 `curr = nxt`。\n3. 当 `curr` 为空时，说明链表已经遍历完毕，此时 `prev` 正好指向反转后的链表头节点，返回 `prev` 即可。",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        \"\"\"
        时间复杂度: O(N) - 遍历一次链表
        空间复杂度: O(1) - 仅使用常数个指针变量
        \"\"\"
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # 暂存当前节点的下一节点，以防链表断裂
            curr.next = prev    # 反转指针方向
            prev = curr         # prev 前移
            curr = nxt          # curr 前移
            
        return prev
"""
    },
    "41_linked_list_cycle.py": {
        "title": "Linked List Cycle (环形链表)",
        "difficulty": "Easy",
        "key_points": "双指针 - 快慢指针 (Floyd's Cycle-Finding Algorithm)",
        "analysis_intuition": "直觉：为了检测链表是否有环，我们可以使用哈希集合 `visited` 来保存我们访问过的所有节点。如果当前节点已经存在于集合中，就说明链表有环。这需要 O(N) 的空间复杂度。是否有 $O(1)$ 空间复杂度的解法？",
        "analysis_derivation": "快慢指针（龟兔赛跑算法）破局：\n我们声明两个指针：\n- 慢指针 `slow`，每次前进一步：`slow = slow.next`。\n- 快指针 `fast`，每次前进两步：`fast = fast.next.next`。\n如果链表没有环，快指针 `fast` 必然会率先走到链表尾部（指向 `None`），程序可以判定无环并返回 `False`。\n如果链表有环，那么快指针和慢指针都会进入环中。由于快指针在环内的速度比慢指针快，它们之间的距离在每一轮循环中都会缩短 1 个节点。最终快指针必定会从后方“追上”慢指针（即 `slow == fast`），就像操场跑道上快跑者套圈慢跑者一样。此时判定有环，返回 `True`。",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        \"\"\"
        时间复杂度: O(N) - 慢指针最多移动 N 次即可判定
        空间复杂度: O(1) - 仅使用两个辅助指针
        \"\"\"
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next         # 慢指针走一步
            fast = fast.next.next    # 快指针走两步
            
            # 如果快慢指针相遇，说明有环
            if slow == fast:
                return True
                
        return False  # 快指针到达尾部，无环
"""
    },
    "42_merge_two_sorted_lists.py": {
        "title": "Merge Two Sorted Lists (合并两个有序链表)",
        "difficulty": "Easy",
        "key_points": "链表合并 / 哑节点 (Dummy Node) 技巧",
        "analysis_intuition": "直觉：我们需要合并两个递增链表，类似于归并排序中的 merge 过程。我们比较两个链表的头节点，取较小的节点连接到新链表上，然后移动指针。",
        "analysis_derivation": "为了避免在初始化新链表头部时进行大量的空指针（null）特殊判断，我们引入一个**哑节点 (Dummy Node)** `dummy`。\n1. 初始化哑节点 `dummy = ListNode(0)`，定义一个指针 `curr` 指向它。\n2. 在 `list1` 和 `list2` 都不为空的循环中，比对两者的值：\n   - 如果 `list1.val <= list2.val`，则将 `curr.next` 连向 `list1`，并将 `list1` 前移。\n   - 否则，将 `curr.next` 连向 `list2`，并将 `list2` 前移。\n   - 接着把新链表的遍历指针 `curr` 前移。\n3. 当循环退出时，必然有一个链表已经处理完毕。我们直接将未处理完的那部分链表接到 `curr.next` 后面（因为有序，无需继续逐个比对）。\n4. 返回 `dummy.next`，即为合并后有序链表的实际头部。",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        \"\"\"
        时间复杂度: O(N + M) - N 和 M 分别为两条链表的长度
        空间复杂度: O(1) - 原地拼接指针，无额外分配空间
        \"\"\"
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
"""
    },
    "43_merge_k_sorted_lists.py": {
        "title": "Merge k Sorted Lists (合并 k 个升序链表)",
        "difficulty": "Hard",
        "key_points": "分治归并 (Divide and Conquer) / 最小堆 (Min-Heap)",
        "analysis_intuition": "直觉：可以利用上一道题的“合并两个有序链表”函数。如果每次把第一条链表跟第二条合并，得到的结果再跟第三条合并... 这种朴素算法的时间复杂度是 O(N * k)，其中 N 是所有节点总数，k 是链表条数，效率较低。",
        "analysis_derivation": "分治法（类似于归并排序）破局：\n不需要挨个合并，我们可以采用**两两配对合并**的方式：\n1. 假设当前有 k 个链表，我们将相邻的链表两两合并（第 0 条和第 1 条合并，第 2 条和第 3 条合并...），将 k 条链表化简为 k/2 条链表。\n2. 重复上述合并过程，链表条数逐渐折半：k/4 -> k/8... 直到只剩下 1 条合并完成的大链表。\n在这种两两分治合并中，合并的总层数为 $\\log k$ 层。每一层中所有的节点都会参与一次合并操作，耗时为 O(N)。因此总时间复杂度被成功优化到 O(N \\log k)。这种迭代的分治策略空间复杂度为 O(1)，优于使用堆（需要额外的堆空间）。",
        "code": """from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        \"\"\"
        时间复杂度: O(N log k) - N 为所有节点总数，k 为链表总个数
        空间复杂度: O(1) - 迭代分治合并仅需常数级额外空间
        \"\"\"
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
"""
    },
    "44_remove_nth_node_from_end_of_list.py": {
        "title": "Remove Nth Node From End of List (删除链表的倒数第 N 个节点)",
        "difficulty": "Medium",
        "key_points": "双指针 - 快慢指针间距控制",
        "analysis_intuition": "直觉：先遍历一次链表，统计链表总长度 L，然后第二次遍历到 L-N 位置的节点，进行删除。但这需要遍历两次链表。如何做到只遍历一次？",
        "analysis_derivation": "双指针一次遍历破局：\n为了删除倒数第 N 个节点，我们必须能够精确定位到**该节点的前一个节点**。我们可以使用间距为 `N` 的两个指针：\n1. 引入哑节点 `dummy` 指向 `head`（处理删除头节点的情况）。\n2. 定义 `fast` 和 `slow` 指针均初始化为 `dummy`。\n3. 先让 `fast` 指针前移 `N + 1` 步。此时 `fast` 和 `slow` 指针之间相差了 `N + 1` 个节点。\n4. 然后，快慢指针以相同速度同步前进，直到 `fast` 指针指向 `None`（链表末尾的下一个位置）。\n5. 此时，`slow` 指针正好停留在**倒数第 N 个节点的前驱节点**上。我们只需执行 `slow.next = slow.next.next` 即可完成对目标节点的删除。\n6. 返回 `dummy.next` 作为新链表的头节点。",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        \"\"\"
        时间复杂度: O(N) - 单次遍历链表
        空间复杂度: O(1)
        \"\"\"
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
"""
    },
    "45_reorder_list.py": {
        "title": "Reorder List (重排链表)",
        "difficulty": "Medium",
        "key_points": "快慢指针求中点 + 链表反转 + 交叉合并",
        "analysis_intuition": "直觉：要将 `L0 -> L1 -> ... -> Ln-1 -> Ln` 重新排列为 `L0 -> Ln -> L1 -> Ln-1 -> ...`。如果直接用数组保存节点，可以容易地利用双指针从两端合并，但这需要 O(N) 的额外空间。能否做到 O(1) 额外空间？",
        "analysis_derivation": "巧妙的链表拆分反转合并三步走：\n我们发现，这个重排实际上是把链表的后半部分逆序之后，与前半部分交叉插入而成的。\n1. **寻找链表的中点**：使用快慢指针，快指针每次走两步，慢指针每次走一步。当快指针到链表尾部时，慢指针所处的位置正好是前半段链表的末尾。我们将链表切分为 `first`（前半部分）和 `second`（后半部分）两段。\n2. **反转后半部分链表**：对 `second` 链表执行就地反转操作，得到逆序后的后半部分链表。\n3. **交叉合并**：将 `first` 和反转后的 `second` 交替连接：把 `second` 的头插在 `first` 第 1 和第 2 个节点之间，然后再移动指针。直至合并完毕。整个过程只需要修改原指针，不需要额外的节点分配。",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \"\"\"
        Do not return anything, modify head in-place instead.
        时间复杂度: O(N) - 找中点、反转、合并各自需要 O(N) 时间
        空间复杂度: O(1) - 原地重构链表
        \"\"\"
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
"""
    }
}
