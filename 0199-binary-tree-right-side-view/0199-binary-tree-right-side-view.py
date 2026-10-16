# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # bfs + inorder (root, left, right)
        if not root:
            return []
        results = []

        queue = deque([root])
        while queue:
            # handle current level
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # put the last node in the current level in the result
                if i == level_size - 1:
                    results.append(node.val)
                # exapnd the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return results

#  TC: O(H*K)
#  SC: O(H*K)