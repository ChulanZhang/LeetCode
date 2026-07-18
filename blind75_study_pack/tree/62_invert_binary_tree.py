from typing import List, Optional, Dict, Set

# Invert Binary Tree - Easy
# 🔑 Key Points: Binary Tree - In-Place Node Swapping
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Inverting a binary tree (mirroring it) means swapping the left child and right child of every node in the tree recursively.
#   - Mathematical Derivation: 
#     1. **Base case**: If the current node `root` is null, return `None`.
#     2. **Swap children**: Swap the left and right pointers of the current node using a parallel assignment: `root.left, root.right = root.right, root.left`.
#     3. **Recursive step**: Recursively invert the left subtree `self.invertTree(root.left)` and the right subtree `self.invertTree(root.right)`.
#     4. Return the mutated `root` node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity: O(N) - Visit every node once
        # Space Complexity: O(H) - Recursion stack space
        if not root:
            return None
            
        # Swap the left and right child pointers
        root.left, root.right = root.right, root.left
        
        # Recursively invert the children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

