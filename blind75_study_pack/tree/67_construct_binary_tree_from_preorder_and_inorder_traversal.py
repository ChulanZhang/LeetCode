from typing import List, Optional, Dict, Set

# Construct Binary Tree from Preorder and Inorder Traversal (从前序与中序遍历序列构造二叉树) - Medium
# 🔑 核心考点: 前中序遍历性质 / 分治递归构建 / 哈希映射定位优化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：前序遍历的第一个元素永远是这棵树（或子树）的**根节点**。而中序遍历中，根节点正好把树分为左子树部分（左边）和右子树部分（右边）。通过结合这两点，我们可以利用分治法递归构建整棵树。
#   - 思维推导: 
#     1. **定位根节点**：在前序数组中取第一个数，它是当前的根节点值 `root_val = preorder[0]`。实例化新节点 `root = TreeNode(root_val)`。
#     2. **切分子树区间**：在中序数组中找到根节点值所在的索引位置 `mid`：
#        - 中序数组中 `mid` 左边的部分是左子树的中序遍历结果。
#        - 右边的部分是右子树的中序遍历结果。
#     3. **计算子树节点数**：左子树有 `left_size = mid` 个节点。因此，在前序数组中，根节点之后的 `left_size` 个元素（即 `preorder[1 : 1 + left_size]`）就是左子树的前序遍历结果，而剩余的部分则是右子树的前序遍历结果。
#     4. **递归并优化**：递归调用上述切分，分别构建 `root.left` 和 `root.right`。在实现中，如果频繁在数组中查找索引或者切片，会导致 $O(N^2)$ 复杂度。我们可以使用一个哈希表 `inorder_map = {val: idx}` 来缓存中序数组的元素索引，并仅传递左右边界指针，将时间复杂度优化到严格的 O(N)。

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        时间复杂度: O(N) - N 为节点总数，借助哈希表实现 O(1) 查找
        空间复杂度: O(N) - 缓存中序数组的哈希表，以及递归调用栈空间
        """
        # 缓存中序遍历的索引映射，避免在递归中重复查找
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # 递归构建的指针版辅助函数
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
                
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 定位中序遍历中的根节点位置
            mid = inorder_map[root_val]
            left_size = mid - in_start  # 左子树包含的节点个数
            
            # 递归构建左子树与右子树
            root.left = build(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            root.right = build(pre_start + left_size + 1, pre_end, mid + 1, in_end)
            
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

