from typing import List, Optional, Dict, Set

# LeetCode 572: Subtree of Another Tree - Easy
# 🔗 Link: https://leetcode.com/problems/subtree-of-another-tree/
# 🔑 Key Points: Binary Tree Recursion - Substructure Matching
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To check if `subRoot` is a subtree of `root`, three cases are possible: 1. `root` and `subRoot` are identical trees. 2. `subRoot` is a subtree of `root.left`. 3. `subRoot` is a subtree of `root.right`.
#   - Mathematical Derivation: 
#     1. Helper `isSameTree(p, q)`: Returns True if two trees have identical structures and values.
#     2. Main function `isSubtree(root, subRoot)`:
#        - If `root` is null, we reached the end of the search path without finding a match. Return False (since `subRoot` is non-empty).
#        - Check `isSameTree(root, subRoot)`. If True, return True.
#        - Otherwise, recursively search in the child nodes: `self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time Complexity: O(M * N) - M, N are node counts. Worst case checks isSame for all root nodes
        # Space Complexity: O(H) - H is height of the root tree (recursion stack depth)
        if not root:
            return False
            
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
            
        # Check if identical at current root, otherwise recurse left and right
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

