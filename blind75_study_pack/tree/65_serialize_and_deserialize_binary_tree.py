from typing import List, Optional, Dict, Set

# Serialize and Deserialize Binary Tree - Hard
# 🔑 Key Points: Pre-Order DFS / Tree Splicing / Serialization Protocol
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To serialize a binary tree into a string and deserialize it back, the serialized string must store the structure (including null nodes) explicitly. A traversal string without null markers cannot uniquely reconstruct a binary tree.
#   - Mathematical Derivation: 
#     Pre-Order DFS (Root -> Left -> Right) Protocol:
#     1. **Serialize**:
#        - Run pre-order DFS on the tree. If a node is null, append a placeholder like `'#'` or `'N'` to the result.
#        - If the node is not null, append its value followed by a delimiter (like `','`).
#        - Example: A tree is serialized to `'1,2,#,#,3,4,#,#,5,#,#'`.
#     2. **Deserialize**:
#        - Split the serialized string by `','` and convert it into a queue `queue`.
#        - Define a recursive helper `dfs(queue)` that dequeues the first element:
#          - If it is `'#'`, return `None`.
#          - Otherwise, instantiate `node = TreeNode(int(val))`.
#          - Recursively construct the left child: `node.left = dfs()`.
#          - Recursively construct the right child: `node.right = dfs()`.
#          - Return `node`.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        # Encodes a tree to a single string.
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        res = []
        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        # Decodes your encoded data to tree.
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        vals = deque(data.split(','))
        
        def dfs():
            val = vals.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            # Construct subtrees in pre-order sequence
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()

