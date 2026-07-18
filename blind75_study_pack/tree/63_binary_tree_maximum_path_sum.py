from typing import List, Optional, Dict, Set

# Binary Tree Maximum Path Sum (二叉树中的最大路径和) - Hard
# 🔑 核心考点: 二叉树后序遍历 (Post-order DFS) / 路径贡献值合并
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：一条二叉树的路径，可能在某个节点处发生“折返”（即包括该节点、它的左子树路径和右子树路径）。对于任何一个节点，如果我们要计算经过它的“折返路径”的最大值，那就是 `node.val + left_gain + right_gain`。但需要注意的是，一个折返路径是无法向上汇报给它的父节点的（因为如果继续向上走，就不能在子节点处折返了，二叉树的路径不能有分支）。
#   - 思维推导: 
#     设计后序 DFS 机制：
#     1. 声明全局变量 `max_sum` 来记录历史最大的折返路径和，初始化为负无穷。
#     2. 对节点进行 DFS，DFS 函数返回当前节点向父节点提供的**单边最大贡献值**（只能选左或者右之一往上连）：
#        - 如果节点为空，贡献值为 0。
#        - 递归计算左子节点的单边贡献 `left = max(0, dfs(node.left))`，小于 0 的贡献抛弃不要，直接当成 0。
#        - 递归计算右子节点的单边贡献 `right = max(0, dfs(node.right))`。
#        - **计算折返路径更新全局最大值**：以当前节点为顶点的最大折返路径和为 `node.val + left + right`，我们用它去更新 `max_sum`。
#        - **向上返回单边贡献值**：由于向上不能有分支，返回给父节点的是 `node.val + max(left, right)`。
#     3. 最终 `max_sum` 记录的即为答案。时间复杂度为 O(N)。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        时间复杂度: O(N) - 每个节点恰好被 DFS 访问一次
        空间复杂度: O(H) - 递归调用栈占用的辅助空间
        """
        max_sum = float('-inf')
        
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
                
            # 计算左右子树能提供的最大单边贡献（如果为负，则选择 0，即不使用该子树）
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # 计算以当前节点为顶点的最大折返路径和，并更新全局最大值
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)
            
            # 返回当前节点向父节点提供的单边最大贡献
            return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return max_sum

