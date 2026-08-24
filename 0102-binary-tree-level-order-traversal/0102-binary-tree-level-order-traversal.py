# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        results = []
        queue = deque([root])

        while queue:
            curr_level = []
            curr_level_length = len(queue)

            for _ in range(curr_level_length):
                node = queue.popleft()
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            results.append(curr_level)
        return results 
