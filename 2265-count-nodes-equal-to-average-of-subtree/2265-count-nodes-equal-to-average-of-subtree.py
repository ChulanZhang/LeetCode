# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        results = 0
        def dfs(node):
            nonlocal results
            if not node:
                return 0, 0
            left_child_sum, left_child_count = dfs(node.left)
            right_child_sum, right_child_count = dfs(node.right)
            total_sum = left_child_sum + node.val + right_child_sum
            total_count = left_child_count + 1 + right_child_count
            if node.val == total_sum//total_count:
                results += 1
            return total_sum, total_count
        dfs(root)
        return results
        