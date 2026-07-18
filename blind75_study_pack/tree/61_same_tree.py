from typing import List, Optional, Dict, Set

# Same Tree - Easy
# 🔑 Key Points: Binary Tree - Synchronous Recursion
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     For two trees to be identical, their root values must be equal, and their left subtrees must be identical, and their right subtrees must be identical. We can compare them using synchronous recursion.
#   - Mathematical Derivation: 
#     Compare two nodes `p` and `q` simultaneously:
#     1. If both `p` and `q` are null, we reached the leaf ends simultaneously with matching structures, return True.
#     2. If only one is null, or their values differ (`p.val != q.val`), they are not identical, return False.
#     3. Otherwise, recursively verify that the left subtrees match `self.isSameTree(p.left, q.left)` and the right subtrees match `self.isSameTree(p.right, q.right)`. Both must be True.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity: O(N) - N is the smaller number of nodes in p and q
        # Space Complexity: O(H) - Recursion stack space
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
        # Check left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

