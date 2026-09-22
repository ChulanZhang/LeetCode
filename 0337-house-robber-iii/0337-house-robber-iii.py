# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob = node.val + left_skip + right_skip
            skip = max(left_rob, left_skip) + max(right_rob, right_skip)

            return rob, skip
        
        return max(dfs(root))