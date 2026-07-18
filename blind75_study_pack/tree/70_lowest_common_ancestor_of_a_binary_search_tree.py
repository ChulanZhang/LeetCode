from typing import List, Optional, Dict, Set

# Lowest Common Ancestor of a Binary Search Tree (二叉搜索树的最近公共祖先) - Medium
# 🔑 核心考点: BST 的大小偏序性质 / 树的自顶向下分岔
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要在 BST 中找到两个节点 `p` 和 `q` 的最近公共祖先（LCA）。我们可以使用常规二叉树的后序遍历 LCA 算法，复杂度为 O(N)。但由于这是一棵二叉搜索树，我们完全可以利用数值大小关系进行快速的分治判定，把时间复杂度降低到 O(H)（在平衡树中为 O(log N)）。
#   - 思维推导: 
#     BST 性质告诉我们：对于任何节点，其左子树的值都小于它，右子树的值都大于它。
#     从根节点 `root` 开始自顶向下迭代检查：
#     1. 如果 `p.val` 和 `q.val` 的值都小于当前 `root.val`，说明这两个目标节点一定都在当前节点的左子树中。我们将 `root` 移动到左孩子：`root = root.left`。
#     2. 如果 `p.val` 和 `q.val` 的值都大于当前 `root.val`，说明它们一定都在当前节点的右子树中。我们将 `root` 移动到右孩子：`root = root.right`。
#     3. **分岔点判定**：如果上面两个条件都不成立（即一个比 `root` 大，一个比 `root` 小；或者其中有一个就是当前 `root` 节点自己），说明在当前节点处，`p` 和 `q` 发生了“分道扬镳”。这个分岔点就是它们的最近公共祖先，直接返回 `root`。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        时间复杂度: O(H) - 沿着单条分支向下搜索，最坏为 O(N)，平衡树时为 O(log N)
        空间复杂度: O(1) - 仅需指针移动，无额外栈开销
        """
        curr = root
        
        while curr:
            # 如果两个目标值都比当前节点小，往左子树走
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # 如果两个目标值都比当前节点大，往右子树走
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                # 出现分岔（或者一个就是当前节点本身），当前节点即为最近公共祖先
                return curr
                
        return None

