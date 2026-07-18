from typing import List, Optional, Dict, Set

# Kth Smallest Element in a BST (二叉搜索树中第 K 小的元素) - Medium
# 🔑 核心考点: 二叉搜索树的中序遍历性质 / 栈迭代早期终止
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：BST（二叉搜索树）有一个非常关键的特性：**对 BST 进行中序遍历（左 -> 根 -> 右），得到的结果刚好是一个严格升序的序列**。所以，寻找第 k 小的元素，就是找出中序遍历中的第 k 个被访问节点。
#   - 思维推导: 
#     为了提高性能并做到早期终止，我们可以使用**迭代版的中序遍历**（用一个显式栈模拟系统递归）：
#     1. 初始化一个空栈 `stack`，当前指针 `curr = root`。
#     2. 在 `curr` 不为空或栈不为空的条件中循环：
#        - **向左倾斜入栈**：一路将当前节点及其所有左侧后代全部压入栈中：`stack.append(curr); curr = curr.left`。这能确保我们总是优先探寻最小的节点。
#        - **出栈处理**：弹出栈顶元素，它就是当前中序遍历中最小的未访问节点。我们对计数器 `k` 减 1（`k -= 1`）。
#        - **早期终止**：如果 `k == 0`，说明找到了第 k 小的元素，直接返回该节点的值。
#        - **转向右子树**：令 `curr = popped_node.right`，准备处理右侧分支。
#     由于使用迭代栈，我们一旦访问完第 k 个元素就立即退出，不会遍历整棵树，极佳地优化了时间复杂度。

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        时间复杂度: O(H + k) - H 是树的高度，需要一路向左压栈，然后向后迭代遍历 k 次
        空间复杂度: O(H) - 栈最大深度等于树的高度
        """
        stack = []
        curr = root
        
        while curr or stack:
            # 1. 一路探寻并入栈最左侧的后代节点
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. 弹出栈顶节点（即当前最小节点）
            curr = stack.pop()
            k -= 1
            
            # 3. 计数达标，早期终止返回
            if k == 0:
                return curr.val
                
            # 4. 转向右子树分支
            curr = curr.right
            
        return -1

