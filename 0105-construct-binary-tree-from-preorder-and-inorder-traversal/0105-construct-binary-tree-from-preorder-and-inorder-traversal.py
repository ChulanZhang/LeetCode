# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # preorder：root -> left -> right
        # inorder: left -> root -> right
        index_map = {val: i for i, val in enumerate(inorder)}  # item lookup from O(n) -> O(1)

        self.preorder_index = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None
            
            # We need to find the root val and set it as a tree node
            root_val = preorder[self.preorder_index]
            
            root = TreeNode(root_val)
            
            self.preorder_index += 1

            mid_index = index_map[root_val]

            root.left = build(in_left, mid_index - 1)
            root.right = build(mid_index + 1, in_right)

            return root
        
        return build(0, len(inorder) - 1)




        