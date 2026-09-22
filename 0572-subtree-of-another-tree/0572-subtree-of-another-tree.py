# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def dfs(left_tree, right_tree):
            if left_tree is None and right_tree is None:
                return True
            
            if left_tree is None or right_tree is None:
                return False
            
            return (
                left_tree.val == right_tree.val and
                dfs(left_tree.left, right_tree.left) and
                dfs(left_tree.right, right_tree.right)
            )
        if root is None:
            return False
        
        return (
            dfs(root, subRoot) or
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )