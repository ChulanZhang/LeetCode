from typing import List, Optional, Dict, Set

# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree - Medium
# 🔗 Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 🔑 Key Points: BST Partial Order / Binary Search-like Node Splitting
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Finding the Lowest Common Ancestor (LCA) in a general binary tree takes O(N) time and O(H) space. However, because this is a Binary Search Tree (BST), we can use the value ordering property to find the LCA in O(H) time and O(1) space.
#   - Mathematical Derivation: 
#     In a BST, a node's left child has a smaller value and its right child has a larger value.
#     Traverse starting from the `root`:
#     1. If both `p.val` and `q.val` are less than the current node's value, the LCA must reside in the left subtree. Move left: `curr = curr.left`.
#     2. If both `p.val` and `q.val` are greater than the current node's value, the LCA must reside in the right subtree. Move right: `curr = curr.right`.
#     3. **Split Point**: If neither condition is met (one value is larger and the other is smaller, or one value equals the current node's value), the paths to `p` and `q` split here. The current node is the LCA. Return it.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time Complexity: O(H) - We traverse down a single branch of the tree. H is O(log N) for balanced trees
        # Space Complexity: O(1) - Constant auxiliary space
        curr = root
        
        while curr:
            # If both targets are in the left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If both targets are in the right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                # Split point found (or current is one of p or q)
                return curr
                
        return None

