# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        def is_leaf(node):
            return not node.left and not node.right
        
        def get_left_boundry(node, res):
            curr = node
            while curr:
                if not is_leaf(curr):
                    res.append(curr.val)
                curr = curr.left if curr.left else curr.right
        
        def get_leaves(node, res):
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            get_leaves(node.left, res)
            get_leaves(node.right, res)

        def get_right_boundry(node, res):
            right_boundry = []  
            curr = node
            while curr:
                if not is_leaf(curr):
                    right_boundry.append(curr.val)
                curr = curr.right if curr.right else curr.left
            res.extend(reversed(right_boundry))
        
        if not root:
            return []
        if is_leaf(root):
            return [root.val]
        
        res = [root.val]
        get_left_boundry(root.left, res)
        get_leaves(root, res)
        get_right_boundry(root.right, res)
        return res