from typing import List, Optional, Dict, Set

# Subtree of Another Tree (另一棵树的子树) - Easy
# 🔑 核心考点: 二叉树递归校验 / 子结构匹配
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要判断 `subRoot` 是不是 `root` 的一个子树，有两种可能：1. `root` 自己和 `subRoot` 是一棵相同的树。 2. `subRoot` 是 `root.left` 的子树。 3. `subRoot` 是 `root.right` 的子树。这又是一个双重递归过程。
#   - 思维推导: 
#     1. 辅助函数 `isSameTree(p, q)`：判断两棵树是否结构和数值完全相同（即 LeetCode 100 题的解法）。
#     2. 主函数 `isSubtree(root, subRoot)`：
#        - 如果 `root` 为空，说明已经走到了底，而 `subRoot` 显然不为空（题目保证 subRoot 至少有一个节点），返回 `False`。
#        - 调用 `isSameTree(root, subRoot)`，如果为 `True`，说明匹配成功，直接返回 `True`。
#        - 否则，递归地在左子树和右子树中寻找匹配：`self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        时间复杂度: O(M * N) - M 和 N 分别为两棵树的节点数。最坏情况下需要以 root 的每个节点为起点运行 SameTree
        空间复杂度: O(H_root) - H_root 为 root 树的高度，系统递归调用栈的深度
        """
        if not root:
            return False
            
        # 辅助判断两棵树是否相同的函数
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
            
        # 检查以当前 root 为头节点是否相同，或者递归去左右子树寻找
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

