from typing import List, Optional, Dict, Set

# LeetCode 102: Binary Tree Level Order Traversal - Medium
# 🔗 Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# 🔑 Key Points: Breadth-First Search (BFS) / Queue Level Splitting
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To output nodes level by level, we use a Breadth-First Search (BFS) facilitated by a queue. When processing a level, we must determine the size of the queue at the start of the level. This allows us to process exactly the nodes belonging to the current level before moving to the next.
#   - Mathematical Derivation: 
#     1. If `root` is null, return an empty list `[]`.
#     2. Initialize a double-ended queue `queue` containing the `root`.
#     3. While the queue is not empty:
#        - Get the number of nodes in the current level: `level_size = len(queue)`.
#        - Iterate `level_size` times. Dequeue a node, append its value to the current level's list `level_nodes`, and enqueue its non-null left and right children.
#        - Append `level_nodes` to the global result list.

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time Complexity: O(N) - Visit every node once
        # Space Complexity: O(N) - Queue holds at most N/2 nodes at the bottom level
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                current_level.append(curr.val)
                # Enqueue children for the next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(current_level)
            
        return res

