from typing import List, Optional, Dict, Set

# Serialize and Deserialize Binary Tree (二叉树的序列化与反序列化) - Hard
# 🔑 核心考点: 前序遍历 (Pre-order DFS) / 字符串编解码 / 树的就地重构
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要将一棵二叉树持久化为字符串，且能够完全反向恢复。这就要求我们在序列化时，必须保留树的“结构信息”（包括空子树的位置），否则仅靠一个遍历结果是无法唯一还原树结构的。
#   - 思维推导: 
#     前序 DFS (根 -> 左 -> 右) 机制：
#     1. **序列化 (Serialize)**：
#        - 对树运行前序 DFS。如果节点为空，我们将其记录为特定的占位符（如 `'#'` 或 `'N'`）。
#        - 如果不为空，记录其值，并逗号分隔。这样，空节点被记录下来就能完整保留树的几何轮廓。
#        - 例如一棵树序列化结果可能为 `'1,2,#,#,3,4,#,#,5,#,#'`。
#     2. **反序列化 (Deserialize)**：
#        - 将生成的序列化字符串按照逗号拆分成一个字符串列表，并转换为一个队列 `queue`。
#        - 我们定义递归恢复函数 `helper(queue)`：每次从队列头部弹出一个元素。
#          - 如果弹出的是 `'#'`，说明这是一个空节点，直接返回 `None`。
#          - 否则，创建一个新节点 `TreeNode(int(val))`。
#          - 然后，**先递归构建左子树，再递归构建右子树**（顺序必须与前序 DFS 写入的顺序完全一致）。
#          - 返回新创建的节点。队列消耗完毕时，整棵树也被完美构建还原。

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        """
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
        """Decodes your encoded data to tree.
        """
        vals = deque(data.split(','))
        
        def dfs():
            val = vals.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            # 严格按照前序遍历顺序递归创建子树
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()

