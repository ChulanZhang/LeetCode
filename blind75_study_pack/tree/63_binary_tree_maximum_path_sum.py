from typing import List, Optional, Dict, Set

# Binary Tree Maximum Path Sum - Hard
# 🔑 Key Points: Post-Order DFS / Path Contribution Merging
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     A path in a binary tree can 'bend' at a node, meaning it can travel from the left subtree, through the node, and into the right subtree. For any node, the maximum sum of a path bending at this node is `node.val + left_gain + right_gain`. However, a path with a bend cannot be extended upward to a parent node because binary tree paths cannot have branches.
#   - Mathematical Derivation: 
#     Post-Order DFS Mechanism:
#     1. Maintain a global variable `max_sum` to store the maximum path sum found, initialized to negative infinity.
#     2. Define a DFS helper that returns the **maximum single-path contribution** the subtree can provide to its parent (i.e. we must choose only *one* branch to extend upward):
#        - If the node is null, return 0.
#        - Calculate the max gain from the left child: `left = max(0, dfs(node.left))`. If a child's gain is negative, we discard it (greedy choice).
#        - Calculate the max gain from the right child: `right = max(0, dfs(node.right))`.
#        - **Calculate the bent path**: The max path sum bending at the current node is `node.val + left + right`. Update `max_sum` with this value.
#        - **Return single-path gain**: Return `node.val + max(left, right)` to the parent node since the path cannot branch.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(N) - Each node is visited exactly once during DFS
        # Space Complexity: O(H) - Auxiliary recursion stack space
        max_sum = float('-inf')
        
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
                
            # Compute maximum single-path gain from left and right children (ignore negative gains)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Update the global maximum path sum considering a path that splits at the current node
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)
            
            # Return the maximum single-path gain (cannot take both left and right to the parent)
            return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return max_sum

