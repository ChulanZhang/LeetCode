# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # bfs
        if not root:
            return []
        results = []
        def bfs(nodes):
            if not nodes:
                return
            tmp = []
            next_level = []
            for node in nodes:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            results.append(tmp)

            bfs(next_level)
        
        bfs([root])
        right_view = []
        for level in results:
            right_view.append(level[-1])
        return right_view