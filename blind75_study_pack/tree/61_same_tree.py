from typing import List, Optional, Dict, Set

# Same Tree (相同的树) - Easy
# 🔑 核心考点: 二叉树同步递归遍历
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要判断两棵树是否完全相同，不仅它们的根节点的值要相等，而且它们的左子树也必须相同，右子树也必须相同。我们可以进行同步的递归比较。
#   - 思维推导: 
#     对两棵树的节点 `p` 和 `q` 进行比对：
#     1. 如果 `p` 和 `q` 都是 `None`，说明两边都走到了底，在此前的比较中完全一致，返回 `True`。
#     2. 如果其中有一个是 `None` 而另一个不是，或者两者的值不相等（`p.val != q.val`），说明树的结构或数值不相同，返回 `False`。
#     3. 如果当前节点一致，则递归验证左子树 `self.isSameTree(p.left, q.left)` 与右子树 `self.isSameTree(p.right, q.right)`。两部分都满足才返回 `True`。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        时间复杂度: O(N) - N 为两棵树中较小的节点总数
        空间复杂度: O(H) - 递归调用栈空间
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

