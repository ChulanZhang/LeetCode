from typing import List, Optional, Dict, Set

# LeetCode 104: Maximum Depth of Binary Tree - Easy
# 🔗 Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 🔑 Key Points: Binary Tree Recursion - Depth-First Search (DFS)
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The maximum depth of a binary tree is the maximum of the depths of its left and right subtrees, plus 1 for the root node itself.
#   - Mathematical Derivation: 
#     We can express this relation recursively:
#     1. **Base case**: If `root` is null, the subtree is empty, so return height 0.
#     2. **Recursion**: Recursively calculate the maximum depth of the left subtree `left_depth` and the right subtree `right_depth`.
#     3. **Combine**: The result is `max(left_depth, right_depth) + 1`.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(N) - Each node is visited exactly once
        # Space Complexity: O(H) - H is the height of the tree, representing the recursion stack depth
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

