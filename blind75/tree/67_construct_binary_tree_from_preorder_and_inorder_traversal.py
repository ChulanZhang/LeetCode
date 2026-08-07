from typing import List, Optional, Dict, Set

# LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal - Medium
# 🔗 Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 🔑 Key Points: Pre-Order & In-Order Properties / Divide and Conquer / Index Mapping
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     In a pre-order traversal, the first element is always the **root node** of the current tree/subtree. In an in-order traversal, the root node partitions the elements into the left subtree (all elements to the left of the root) and the right subtree (all elements to the right). We can use this property to recursively rebuild the tree.
#   - Mathematical Derivation: 
#     1. **Root Extraction**: The first element in preorder is the root value: `root_val = preorder[pre_start]`. Instantiate `root = TreeNode(root_val)`.
#     2. **Partitioning**: Locate the index of `root_val` in inorder, say `mid`. The elements to the left of `mid` represent the left subtree, and elements to the right represent the right subtree.
#     3. **Subproblem division**: The left subtree has size `left_size = mid - in_start`. Thus, the left subtree's preorder values are located at indices `[pre_start + 1 ... pre_start + left_size]`, and the right subtree's preorder values are at indices `[pre_start + left_size + 1 ... pre_end]`.
#     4. **Optimization**: Slicing arrays in recursion takes O(N^2) time. We optimize this to O(N) by storing inorder values in a hash map (`inorder_map = {val: idx}`) for O(1) index lookup and passing boundary pointers in recursion.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time Complexity: O(N) - N is the number of nodes. Hash map index lookup is O(1)
        # Space Complexity: O(N) - Hash map storage and recursion call stack
        
        # Cache inorder indices to avoid O(N) searches during recursion
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
                
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Locate root in inorder list
            mid = inorder_map[root_val]
            left_size = mid - in_start  # Number of nodes in left subtree
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            root.right = build(pre_start + left_size + 1, pre_end, mid + 1, in_end)
            
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

