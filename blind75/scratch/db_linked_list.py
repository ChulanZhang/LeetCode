# Linked List category data
PROBLEMS = {
    "40_reverse_linked_list.py": {
        "title": "Reverse Linked List",
        "difficulty": "Easy",
        "key_points": "Linked List Basics - Two Pointers Iterative",
        "analysis_intuition": "To reverse a singly linked list, we need to alter the direction of each node's pointer. Specifically, we change the `next` pointer of each node to point to its predecessor `prev`. Since it's a singly linked list, changing the `next` pointer causes us to lose the reference to the rest of the list. Thus, we must temporarily store the next node before modifying the current pointer.",
        "analysis_derivation": "1. Initialize two pointers: `curr` pointing to the head node, and `prev` initialized to `None` (as the new tail should point to null).\n2. Traverse the list:\n   - **Preserve successor**: Store the next node: `nxt = curr.next`.\n   - **Reverse link**: Point the current node back to the predecessor: `curr.next = prev`.\n   - **Advance pointers**: Shift `prev` to `curr` (`prev = curr`) and `curr` to the stored successor (`curr = nxt`).\n3. When `curr` becomes null, the traversal is complete, and `prev` points to the new head of the reversed list. Return `prev`.",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(N) - Single pass through the linked list
        # Space Complexity: O(1) - Constant pointer variables
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # Temporarily store the next node to prevent disconnection
            curr.next = prev    # Reverse current node's pointer
            prev = curr         # Shift prev pointer forward
            curr = nxt          # Shift curr pointer forward
            
        return prev
"""
    },
    "41_linked_list_cycle.py": {
        "title": "Linked List Cycle",
        "difficulty": "Easy",
        "key_points": "Two Pointers - Fast & Slow Pointers (Floyd's Cycle-Finding Algorithm)",
        "analysis_intuition": "To detect if a linked list contains a cycle, we could store visited nodes in a hash set. If we encounter a node already in the set, a cycle exists. However, this takes O(N) auxiliary space. Can we solve this in O(1) space?",
        "analysis_derivation": "Floyd's Cycle-Finding Algorithm (Tortoise and Hare):\nInitialize two pointers at the head:\n- Slow pointer `slow` moves 1 step at a time: `slow = slow.next`.\n- Fast pointer `fast` moves 2 steps at a time: `fast = fast.next.next`.\nIf the list is acyclic, `fast` will eventually reach the end of the list (null), and we can return False.\nIf the list contains a cycle, both pointers will eventually enter the loop. Since `fast` is moving twice as fast as `slow`, the relative distance between them decreases by 1 in each step. Consequently, `fast` will eventually catch up to (or lap) `slow` inside the loop (i.e., `slow == fast`), at which point we return True.",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(N) - Slow pointer moves at most N steps
        # Space Complexity: O(1) - Only two pointers are allocated
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next         # Slow pointer moves 1 step
            fast = fast.next.next    # Fast pointer moves 2 steps
            
            # If pointers meet, a cycle exists
            if slow == fast:
                return True
                
        return False  # Fast pointer reached the end of the list, no cycle
"""
    },
    "42_merge_two_sorted_lists.py": {
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy",
        "key_points": "Linked List Merging / Dummy Node Technique",
        "analysis_intuition": "To merge two sorted lists, we compare their heads and connect the smaller node to the merged list, advancing that list's pointer. This is similar to the merge step in Merge Sort.",
        "analysis_derivation": "To avoid complex edge cases when initializing the head of the merged list, we use a **Dummy Node** `dummy`:\n1. Initialize `dummy = ListNode(0)` and a traversal pointer `curr = dummy`.\n2. While both `list1` and `list2` are not null:\n   - Compare `list1.val` and `list2.val`.\n   - Connect `curr.next` to the node with the smaller value, then advance that list's pointer.\n   - Advance `curr`.\n3. Once the loop terminates, at least one list is exhausted. We append the remaining elements of the non-empty list directly to `curr.next` since they are already sorted.\n4. Return `dummy.next`.",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(N + M) - N and M are the lengths of the two lists
        # Space Complexity: O(1) - Merging is done in-place by splicing pointers
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # Append the remaining nodes of the non-empty list
        curr.next = list1 if list1 else list2
        
        return dummy.next
"""
    },
    "43_merge_k_sorted_lists.py": {
        "title": "Merge k Sorted Lists",
        "difficulty": "Hard",
        "key_points": "Divide and Conquer / Min-Heap",
        "analysis_intuition": "We can reuse the logic of merging two sorted lists. Merging lists sequentially (e.g., merging list 1 with list 2, then the result with list 3, and so on) has an inefficient time complexity of O(N * k), where N is the total number of nodes and k is the number of lists.",
        "analysis_derivation": "Divide and Conquer (similar to Merge Sort):\nInstead of merging sequentially, we merge lists in pairs:\n1. Group the k lists into pairs and merge each pair. This reduces the number of lists from k to k/2.\n2. Repeat this process recursively/iteratively: k/2 -> k/4 -> k/8... until only 1 merged list remains.\nIn this divide and conquer approach, the total merge height is $\\log k$ levels. At each level, every node is merged once, taking O(N) time. Thus, the overall time complexity is optimized to O(N \\log k). This iterative method has O(1) auxiliary space complexity, which is superior to min-heap solutions that require extra heap memory.",
        "code": """from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time Complexity: O(N log k) - N is the total number of nodes, k is the number of lists
        # Space Complexity: O(1) - Iterative divide and conquer merges in-place
        if not lists:
            return None
            
        # Helper function to merge two sorted lists
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
            
        # Pairwise iterative divide and conquer merge
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
        "title": "Remove Nth Node From End of List",
        "difficulty": "Medium",
        "key_points": "Two Pointers - Fast & Slow Pointers Gap Control",
        "analysis_intuition": "A naive approach is to perform a first pass to count the list length L, and a second pass to traverse to the (L-N)-th node to remove it. This requires scanning the list twice. How can we achieve this in a single pass?",
        "analysis_derivation": "Two Pointers in a Single Pass:\nTo remove the N-th node from the end, we need to locate its **immediate predecessor**. We can maintain a gap of `N` nodes between two pointers:\n1. Initialize a `dummy` node pointing to `head` (to handle cases where the head itself is removed).\n2. Place `fast` and `slow` pointers at the `dummy` node.\n3. Advance `fast` by `N + 1` steps. This establishes a gap of `N + 1` nodes between `fast` and `slow`.\n4. Advance both pointers at the same speed until `fast` reaches null (the end of the list).\n5. At this point, `slow` will be pointing exactly to the predecessor of the target node. We remove the target node by executing `slow.next = slow.next.next`.\n6. Return `dummy.next`.",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time Complexity: O(N) - Single pass traversal
        # Space Complexity: O(1)
        dummy = ListNode(0, head)  # Dummy node to handle deletion of head node
        fast = dummy
        slow = dummy
        
        # Advance fast pointer by n + 1 steps to create a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers simultaneously until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # slow now points to the node preceding the target. Delete the target node.
        slow.next = slow.next.next
        
        return dummy.next
"""
    },
    "45_reorder_list.py": {
        "title": "Reorder List",
        "difficulty": "Medium",
        "key_points": "Find Midpoint (Fast & Slow Pointers) + Reverse List + Interleave Merge",
        "analysis_intuition": "Reorder the list `L0 -> L1 -> ... -> Ln-1 -> Ln` to `L0 -> Ln -> L1 -> Ln-1 -> ...`. Using an auxiliary array to store nodes makes this trivial but requires O(N) extra space. We need an O(1) space solution.",
        "analysis_derivation": "Three-Step Splicing:\nNotice that the reordered list is formed by taking the second half of the list, reversing it, and interleaving it with the first half.\n1. **Find midpoint**: Use fast/slow pointers. When the fast pointer reaches the end, the slow pointer points to the midpoint. Split the list into `first_half` and `second_half`.\n2. **Reverse second half**: Reverse the `second_half` in-place.\n3. **Interleave merge**: Interleave nodes from `first_half` and the reversed `second_half` one by one by adjusting their pointers. This requires no extra memory allocation.",
        "code": """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Do not return anything, modify head in-place instead.
        # Time Complexity: O(N) - Finding midpoint, reversing, and merging take O(N) combined
        # Space Complexity: O(1) - Pointers modified in-place
        if not head or not head.next:
            return
            
        # 1. Find midpoint using fast/slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow points to the midpoint. Split the list.
        second_half = slow.next
        slow.next = None  # Disconnect first half from second half
        
        # 2. Reverse the second half of the list in-place
        prev = None
        curr = second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second_half = prev  # Head of the reversed second half
        
        # 3. Interleave the first half and reversed second half
        first_half = head
        while first_half and second_half:
            # Store successors
            tmp1 = first_half.next
            tmp2 = second_half.next
            
            # Interleave pointers
            first_half.next = second_half
            second_half.next = tmp1
            
            # Advance pointers
            first_half = tmp1
            second_half = tmp2
"""
    }
}
