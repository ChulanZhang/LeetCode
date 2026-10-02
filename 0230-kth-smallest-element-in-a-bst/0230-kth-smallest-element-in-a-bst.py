# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # inorder: left -> root -> right
        results = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            results.append(node.val)
            inorder(node.right)

        inorder(root)
        return results[k-1]
        