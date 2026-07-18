from typing import List, Optional, Dict, Set

# Kth Smallest Element in a BST - Medium
# 🔑 Key Points: BST In-Order Traversal Properties / Iterative Stack with Early Termination
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     An in-order traversal (Left -> Root -> Right) of a Binary Search Tree (BST) visits nodes in strictly ascending order. Thus, finding the k-th smallest element is equivalent to finding the k-th node visited during an in-order traversal.
#   - Mathematical Derivation: 
#     To optimize performance, we use an **iterative in-order traversal** utilizing an explicit stack. This allows us to stop the traversal immediately once the k-th element is reached:
#     1. Initialize an empty stack and set `curr = root`.
#     2. In a loop while `curr` is not null or the stack is not empty:
#        - **Go left**: Push the current node and all its left descendants onto the stack: `stack.append(curr); curr = curr.left`. This ensures we always process the smallest element next.
#        - **Pop and process**: Pop from the stack. This is the next smallest element in in-order. Decrement `k` by 1.
#        - **Check target**: If `k == 0`, we have found the k-th smallest element. Return its value immediately.
#        - **Go right**: Set `curr = popped_node.right` to process its right subtree.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time Complexity: O(H + k) - H is the height of the tree. We traverse down to the leftmost leaf, then perform k pop operations
        # Space Complexity: O(H) - Stack stores at most H nodes
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Travel to the leftmost node, pushing all nodes along the path to the stack
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. Process the top of the stack (smallest unvisited node)
            curr = stack.pop()
            k -= 1
            
            # 3. If we've popped k elements, we have found the target
            if k == 0:
                return curr.val
                
            # 4. Move to the right child
            curr = curr.right
            
        return -1

