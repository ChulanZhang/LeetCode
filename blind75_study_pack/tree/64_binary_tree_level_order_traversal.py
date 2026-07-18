from typing import List, Optional, Dict, Set

# Binary Tree Level Order Traversal (二叉树的层序遍历) - Medium
# 🔑 核心考点: 广度优先搜索 (BFS) / 队列 (Queue) 按层切分
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要按层输出二叉树的节点。我们应该使用广度优先搜索 (BFS)，用队列来辅助遍历节点。在处理每一层时，我们需要一次性清空当前队列中属于该层的所有节点，这样就能区分开不同层的输出。
#   - 思维推导: 
#     1. 如果 `root` 为空，返回空列表 `[]`。
#     2. 初始化队列 `queue` 并将 `root` 入队。
#     3. 当队列不为空时：
#        - 获取当前层包含的节点数 `level_size = len(queue)`。这代表了这批出队元素全部属于同一层。
#        - 循环 `level_size` 次，弹出队首节点，将其值加入当前层的列表 `level_nodes` 中，并将其不为空的左右孩子节点依次加入队列尾部。
#        - 将当前层的结果 `level_nodes` 加入全局结果集中。
#     4. 循环结束时，结果集中就以二维列表的形式保存了按层划分的节点值。

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        时间复杂度: O(N) - 遍历所有节点各一次
        空间复杂度: O(N) - 队列中最多同时存放最底层一层的节点（约 N/2 个）
        """
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # 记录当前层的节点数
            current_level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                current_level.append(curr.val)
                # 依次将非空子节点加入队列，参与下一层的遍历
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(current_level)
            
        return res

