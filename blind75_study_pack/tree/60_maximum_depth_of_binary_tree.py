from typing import List, Optional, Dict, Set

# Maximum Depth of Binary Tree (二叉树的最大深度) - Easy
# 🔑 核心考点: 二叉树递归遍历 - 深度优先搜索 (DFS)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：一棵二叉树的最大深度等于它的左子树和右子树最大深度中的较大值，加上根节点本身的这一层高度（即 1）。
#   - 思维推导: 
#     可以使用简单的递归 DFS 来描述这一结构关系：
#     1. **基准情况**：如果当前节点 `root` 为空，说明已经越过叶子节点，返回高度 `0`。
#     2. **递归子问题**：递归计算左子树的最大深度 `left_depth`，以及右子树的最大深度 `right_depth`。
#     3. **合并结果**：返回 `max(left_depth, right_depth) + 1`。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        时间复杂度: O(N) - 每个节点恰好访问一次
        空间复杂度: O(H) - H 为树的高度，递归系统调用栈的深度
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

