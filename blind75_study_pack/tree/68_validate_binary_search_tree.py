from typing import List, Optional, Dict, Set

# LeetCode 98: Validate Binary Search Tree - Medium
# 🔗 Link: https://leetcode.com/problems/validate-binary-search-tree/
# 🔑 Key Points: BST Definition - Interval Bounds DFS Propagation
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A common mistake is validating only that a node is greater than its left child and smaller than its right child. This is incorrect. In a Binary Search Tree (BST), **all nodes in the left subtree must be less than the parent node, and all nodes in the right subtree must be greater than the parent node**.
#   - Mathematical Derivation: 
#     To enforce this definition globally, we propagate valid open intervals `(lower, upper)` down during DFS:
#     1. Initialize `validate(root, -inf, inf)`.
#     2. In each step:
#        - If the node is null, return True.
#        - Verify if the node's value falls inside the open interval: `lower < node.val < upper`. If not, return False.
#        - **Update bounds for children**:
#          - When validating the left child, its value must be less than the current node's value. The upper bound shifts to `node.val`: `validate(node.left, lower, node.val)`.
#          - When validating the right child, its value must be greater than the current node's value. The lower bound shifts to `node.val`: `validate(node.right, node.val, upper)`.
#        - Return True if both children are valid BSTs.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity: O(N) - Visit every node once
        # Space Complexity: O(H) - Recursion stack space
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
                
            # Node value must be strictly within the allowed range
            if not (lower < node.val < upper):
                return False
                
            # Left child values must be in (lower, node.val); right child values in (node.val, upper)
            return (validate(node.left, lower, node.val) and 
                    validate(node.right, node.val, upper))
                    
        return validate(root)

