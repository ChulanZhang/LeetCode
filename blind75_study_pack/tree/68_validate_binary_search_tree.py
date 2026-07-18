from typing import List, Optional, Dict, Set

# Validate Binary Search Tree (验证二叉搜索树) - Medium
# 🔑 核心考点: 二叉搜索树 (BST) 的性质定义 / 区间边界传递递归
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：很多同学容易走进一个误区：只判定每个节点是否大于左孩子且小于右孩子。这是不够的。因为在 BST 中，**左子树的所有节点都必须小于当前节点，右子树的所有节点都必须大于当前节点**。例如，`[10, 5, 15, None, None, 6, 20]`，节点 6 虽然大于 5，但它在根节点 10 的右子树却小于 10，这违反了 BST 定义。
#   - 思维推导: 
#     区间边界传递破局：
#     我们需要在递归时向下传递每个节点必须满足的**上限（upper）和下限（lower）值范围**。
#     1. 初始化调用 `dfs(root, -inf, inf)`，根节点可以为任意值。
#     2. 在递归的每一步中：
#        - 如果当前节点 `node` 为空，返回 `True`。
#        - 检查当前节点的值是否满足边界：`lower < node.val < upper`。若不满足，说明非法，返回 `False`。
#        - **向下更新边界**：
#          - 当向左子树递归时，所有左节点都必须小于当前节点。因此上限更新为当前节点的值：`dfs(node.left, lower, node.val)`。
#          - 当向右子树递归时，所有右节点都必须大于当前节点。因此下限更新为当前节点的值：`dfs(node.right, node.val, upper)`。
#        - 左右两边都合法才返回 `True`。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        时间复杂度: O(N) - 遍历所有节点一次
        空间复杂度: O(H) - 递归调用栈空间
        """
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
                
            # 当前节点值必须落在合法的开放区间内
            if not (lower < node.val < upper):
                return False
                
            # 左子树所有节点值必须小于 node.val，右子树所有节点值必须大于 node.val
            return (validate(node.left, lower, node.val) and 
                    validate(node.right, node.val, upper))
                    
        return validate(root)

