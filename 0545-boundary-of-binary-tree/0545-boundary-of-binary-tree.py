# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        results = [root.val]
        if not root.left and not root.right:
            return results

        curr = root.left
        while curr:
            if curr.left or curr.right:
                results.append(curr.val)
            curr = curr.left if curr.left else curr.right
        
        def add_leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                results.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        add_leaves(root)

        right_boundry = []
        curr = root.right
        while curr:
            if curr.left or curr.right:
                right_boundry.append(curr.val)
            curr = curr.right if curr.right else curr.left
        
        results.extend(right_boundry[::-1])
        
        return results


        