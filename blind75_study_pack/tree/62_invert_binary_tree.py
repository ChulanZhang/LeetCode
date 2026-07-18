from typing import List, Optional, Dict, Set

# Invert Binary Tree (翻转二叉树) - Easy
# 🔑 核心考点: 二叉树遍历结构就地修改 (In-place swap)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：翻转一棵二叉树（镜像对称），实际上就是把每个节点的左孩子和右孩子进行对调，然后再递归地翻转它们的子树。
#   - 思维推导: 
#     1. **基准情况**：如果当前节点 `root` 为空，直接返回 `None`。
#     2. **交换左右子树**：直接使用 Python 的并口赋值语句，交换当前节点的左右子节点：`root.left, root.right = root.right, root.left`。
#     3. **递归处理**：递归地翻转左子树 `self.invertTree(root.left)` 和右子树 `self.invertTree(root.right)`。
#     4. 返回当前节点 `root`。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        时间复杂度: O(N) - 遍历所有节点一次
        空间复杂度: O(H) - 递归系统栈空间
        """
        if not root:
            return None
            
        # 交换左右子树指针
        root.left, root.right = root.right, root.left
        
        # 递归翻转子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

