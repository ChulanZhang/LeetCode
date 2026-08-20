# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # inorder method to collect all elements in the tree
        # nums = []
        # def inorder(node):
        #     if not node:
        #         return
        #     inorder(node.left)
        #     nums.append(node.val)
        #     inorder(node.right)
        
        # inorder(root)

        # left, right = 0, len(nums) - 1

        # while left < right:
        #     total = nums[left] + nums[right]

        #     if total == k:
        #         return True
        #     elif total > k:
        #         right -= 1
        #     else:
        #         left += 1
            
        # return False

        seen = set()

        def dfs(node):
            if not node:
                return False

            if k - node.val in seen:
                return True
            else:
                seen.add(node.val)
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

# TC: O(n)
# SC: O(n)