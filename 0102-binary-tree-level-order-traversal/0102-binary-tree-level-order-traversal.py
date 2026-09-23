# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        def dfs(node, level):
            if not node:
                return
            if len(results) == level:
                results.append([])
            results[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return results
        # if not root:
        #     return []
        # results = []
        # def bfs(nodes):
        #     if not nodes:
        #         return
        #     tmp = []
        #     next_level = []
        #     for node in nodes:
        #         tmp.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     results.append(tmp)

        #     bfs(next_level)

        # bfs([root])
        # return results
