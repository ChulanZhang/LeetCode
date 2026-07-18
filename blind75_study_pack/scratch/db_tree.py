# Tree category data
PROBLEMS = {
    "60_maximum_depth_of_binary_tree.py": {
        "title": "Maximum Depth of Binary Tree (二叉树的最大深度)",
        "difficulty": "Easy",
        "key_points": "二叉树递归遍历 - 深度优先搜索 (DFS)",
        "analysis_intuition": "直觉：一棵二叉树的最大深度等于它的左子树和右子树最大深度中的较大值，加上根节点本身的这一层高度（即 1）。",
        "analysis_derivation": "可以使用简单的递归 DFS 来描述这一结构关系：\n1. **基准情况**：如果当前节点 `root` 为空，说明已经越过叶子节点，返回高度 `0`。\n2. **递归子问题**：递归计算左子树的最大深度 `left_depth`，以及右子树的最大深度 `right_depth`。\n3. **合并结果**：返回 `max(left_depth, right_depth) + 1`。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        \"\"\"
        时间复杂度: O(N) - 每个节点恰好访问一次
        空间复杂度: O(H) - H 为树的高度，递归系统调用栈的深度
        \"\"\"
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""
    },
    "61_same_tree.py": {
        "title": "Same Tree (相同的树)",
        "difficulty": "Easy",
        "key_points": "二叉树同步递归遍历",
        "analysis_intuition": "直觉：要判断两棵树是否完全相同，不仅它们的根节点的值要相等，而且它们的左子树也必须相同，右子树也必须相同。我们可以进行同步的递归比较。",
        "analysis_derivation": "对两棵树的节点 `p` 和 `q` 进行比对：\n1. 如果 `p` 和 `q` 都是 `None`，说明两边都走到了底，在此前的比较中完全一致，返回 `True`。\n2. 如果其中有一个是 `None` 而另一个不是，或者两者的值不相等（`p.val != q.val`），说明树的结构或数值不相同，返回 `False`。\n3. 如果当前节点一致，则递归验证左子树 `self.isSameTree(p.left, q.left)` 与右子树 `self.isSameTree(p.right, q.right)`。两部分都满足才返回 `True`。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        \"\"\"
        时间复杂度: O(N) - N 为两棵树中较小的节点总数
        空间复杂度: O(H) - 递归调用栈空间
        \"\"\"
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
"""
    },
    "62_invert_binary_tree.py": {
        "title": "Invert Binary Tree (翻转二叉树)",
        "difficulty": "Easy",
        "key_points": "二叉树遍历结构就地修改 (In-place swap)",
        "analysis_intuition": "直觉：翻转一棵二叉树（镜像对称），实际上就是把每个节点的左孩子和右孩子进行对调，然后再递归地翻转它们的子树。",
        "analysis_derivation": "1. **基准情况**：如果当前节点 `root` 为空，直接返回 `None`。\n2. **交换左右子树**：直接使用 Python 的并口赋值语句，交换当前节点的左右子节点：`root.left, root.right = root.right, root.left`。\n3. **递归处理**：递归地翻转左子树 `self.invertTree(root.left)` 和右子树 `self.invertTree(root.right)`。\n4. 返回当前节点 `root`。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        \"\"\"
        时间复杂度: O(N) - 遍历所有节点一次
        空间复杂度: O(H) - 递归系统栈空间
        \"\"\"
        if not root:
            return None
            
        # 交换左右子树指针
        root.left, root.right = root.right, root.left
        
        # 递归翻转子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
"""
    },
    "63_binary_tree_maximum_path_sum.py": {
        "title": "Binary Tree Maximum Path Sum (二叉树中的最大路径和)",
        "difficulty": "Hard",
        "key_points": "二叉树后序遍历 (Post-order DFS) / 路径贡献值合并",
        "analysis_intuition": "直觉：一条二叉树的路径，可能在某个节点处发生“折返”（即包括该节点、它的左子树路径和右子树路径）。对于任何一个节点，如果我们要计算经过它的“折返路径”的最大值，那就是 `node.val + left_gain + right_gain`。但需要注意的是，一个折返路径是无法向上汇报给它的父节点的（因为如果继续向上走，就不能在子节点处折返了，二叉树的路径不能有分支）。",
        "analysis_derivation": "设计后序 DFS 机制：\n1. 声明全局变量 `max_sum` 来记录历史最大的折返路径和，初始化为负无穷。\n2. 对节点进行 DFS，DFS 函数返回当前节点向父节点提供的**单边最大贡献值**（只能选左或者右之一往上连）：\n   - 如果节点为空，贡献值为 0。\n   - 递归计算左子节点的单边贡献 `left = max(0, dfs(node.left))`，小于 0 的贡献抛弃不要，直接当成 0。\n   - 递归计算右子节点的单边贡献 `right = max(0, dfs(node.right))`。\n   - **计算折返路径更新全局最大值**：以当前节点为顶点的最大折返路径和为 `node.val + left + right`，我们用它去更新 `max_sum`。\n   - **向上返回单边贡献值**：由于向上不能有分支，返回给父节点的是 `node.val + max(left, right)`。\n3. 最终 `max_sum` 记录的即为答案。时间复杂度为 O(N)。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        \"\"\"
        时间复杂度: O(N) - 每个节点恰好被 DFS 访问一次
        空间复杂度: O(H) - 递归调用栈占用的辅助空间
        \"\"\"
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
"""
    },
    "64_binary_tree_level_order_traversal.py": {
        "title": "Binary Tree Level Order Traversal (二叉树的层序遍历)",
        "difficulty": "Medium",
        "key_points": "广度优先搜索 (BFS) / 队列 (Queue) 按层切分",
        "analysis_intuition": "直觉：要按层输出二叉树的节点。我们应该使用广度优先搜索 (BFS)，用队列来辅助遍历节点。在处理每一层时，我们需要一次性清空当前队列中属于该层的所有节点，这样就能区分开不同层的输出。",
        "analysis_derivation": "1. 如果 `root` 为空，返回空列表 `[]`。\n2. 初始化队列 `queue` 并将 `root` 入队。\n3. 当队列不为空时：\n   - 获取当前层包含的节点数 `level_size = len(queue)`。这代表了这批出队元素全部属于同一层。\n   - 循环 `level_size` 次，弹出队首节点，将其值加入当前层的列表 `level_nodes` 中，并将其不为空的左右孩子节点依次加入队列尾部。\n   - 将当前层的结果 `level_nodes` 加入全局结果集中。\n4. 循环结束时，结果集中就以二维列表的形式保存了按层划分的节点值。",
        "code": """from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        \"\"\"
        时间复杂度: O(N) - 遍历所有节点各一次
        空间复杂度: O(N) - 队列中最多同时存放最底层一层的节点（约 N/2 个）
        \"\"\"
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
"""
    },
    "65_serialize_and_deserialize_binary_tree.py": {
        "title": "Serialize and Deserialize Binary Tree (二叉树的序列化与反序列化)",
        "difficulty": "Hard",
        "key_points": "前序遍历 (Pre-order DFS) / 字符串编解码 / 树的就地重构",
        "analysis_intuition": "直觉：我们需要将一棵二叉树持久化为字符串，且能够完全反向恢复。这就要求我们在序列化时，必须保留树的“结构信息”（包括空子树的位置），否则仅靠一个遍历结果是无法唯一还原树结构的。",
        "analysis_derivation": "前序 DFS (根 -> 左 -> 右) 机制：\n1. **序列化 (Serialize)**：\n   - 对树运行前序 DFS。如果节点为空，我们将其记录为特定的占位符（如 `'#'` 或 `'N'`）。\n   - 如果不为空，记录其值，并逗号分隔。这样，空节点被记录下来就能完整保留树的几何轮廓。\n   - 例如一棵树序列化结果可能为 `'1,2,#,#,3,4,#,#,5,#,#'`。\n2. **反序列化 (Deserialize)**：\n   - 将生成的序列化字符串按照逗号拆分成一个字符串列表，并转换为一个队列 `queue`。\n   - 我们定义递归恢复函数 `helper(queue)`：每次从队列头部弹出一个元素。\n     - 如果弹出的是 `'#'`，说明这是一个空节点，直接返回 `None`。\n     - 否则，创建一个新节点 `TreeNode(int(val))`。\n     - 然后，**先递归构建左子树，再递归构建右子树**（顺序必须与前序 DFS 写入的顺序完全一致）。\n     - 返回新创建的节点。队列消耗完毕时，整棵树也被完美构建还原。",
        "code": """from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        \"\"\"Encodes a tree to a single string.
        \"\"\"
        res = []
        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        \"\"\"Decodes your encoded data to tree.
        \"\"\"
        vals = deque(data.split(','))
        
        def dfs():
            val = vals.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            # 严格按照前序遍历顺序递归创建子树
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()
"""
    },
    "66_subtree_of_another_tree.py": {
        "title": "Subtree of Another Tree (另一棵树的子树)",
        "difficulty": "Easy",
        "key_points": "二叉树递归校验 / 子结构匹配",
        "analysis_intuition": "直觉：要判断 `subRoot` 是不是 `root` 的一个子树，有两种可能：1. `root` 自己和 `subRoot` 是一棵相同的树。 2. `subRoot` 是 `root.left` 的子树。 3. `subRoot` 是 `root.right` 的子树。这又是一个双重递归过程。",
        "analysis_derivation": "1. 辅助函数 `isSameTree(p, q)`：判断两棵树是否结构和数值完全相同（即 LeetCode 100 题的解法）。\n2. 主函数 `isSubtree(root, subRoot)`：\n   - 如果 `root` 为空，说明已经走到了底，而 `subRoot` 显然不为空（题目保证 subRoot 至少有一个节点），返回 `False`。\n   - 调用 `isSameTree(root, subRoot)`，如果为 `True`，说明匹配成功，直接返回 `True`。\n   - 否则，递归地在左子树和右子树中寻找匹配：`self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        \"\"\"
        时间复杂度: O(M * N) - M 和 N 分别为两棵树的节点数。最坏情况下需要以 root 的每个节点为起点运行 SameTree
        空间复杂度: O(H_root) - H_root 为 root 树的高度，系统递归调用栈的深度
        \"\"\"
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
"""
    },
    "67_construct_binary_tree_from_preorder_and_inorder_traversal.py": {
        "title": "Construct Binary Tree from Preorder and Inorder Traversal (从前序与中序遍历序列构造二叉树)",
        "difficulty": "Medium",
        "key_points": "前中序遍历性质 / 分治递归构建 / 哈希映射定位优化",
        "analysis_intuition": "直觉：前序遍历的第一个元素永远是这棵树（或子树）的**根节点**。而中序遍历中，根节点正好把树分为左子树部分（左边）和右子树部分（右边）。通过结合这两点，我们可以利用分治法递归构建整棵树。",
        "analysis_derivation": "1. **定位根节点**：在前序数组中取第一个数，它是当前的根节点值 `root_val = preorder[0]`。实例化新节点 `root = TreeNode(root_val)`。\n2. **切分子树区间**：在中序数组中找到根节点值所在的索引位置 `mid`：\n   - 中序数组中 `mid` 左边的部分是左子树的中序遍历结果。\n   - 右边的部分是右子树的中序遍历结果。\n3. **计算子树节点数**：左子树有 `left_size = mid` 个节点。因此，在前序数组中，根节点之后的 `left_size` 个元素（即 `preorder[1 : 1 + left_size]`）就是左子树的前序遍历结果，而剩余的部分则是右子树的前序遍历结果。\n4. **递归并优化**：递归调用上述切分，分别构建 `root.left` 和 `root.right`。在实现中，如果频繁在数组中查找索引或者切片，会导致 $O(N^2)$ 复杂度。我们可以使用一个哈希表 `inorder_map = {val: idx}` 来缓存中序数组的元素索引，并仅传递左右边界指针，将时间复杂度优化到严格的 O(N)。",
        "code": """from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        \"\"\"
        时间复杂度: O(N) - N 为节点总数，借助哈希表实现 O(1) 查找
        空间复杂度: O(N) - 缓存中序数组的哈希表，以及递归调用栈空间
        \"\"\"
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
"""
    },
    "68_validate_binary_search_tree.py": {
        "title": "Validate Binary Search Tree (验证二叉搜索树)",
        "difficulty": "Medium",
        "key_points": "二叉搜索树 (BST) 的性质定义 / 区间边界传递递归",
        "analysis_intuition": "直觉：很多同学容易走进一个误区：只判定每个节点是否大于左孩子且小于右孩子。这是不够的。因为在 BST 中，**左子树的所有节点都必须小于当前节点，右子树的所有节点都必须大于当前节点**。例如，`[10, 5, 15, None, None, 6, 20]`，节点 6 虽然大于 5，但它在根节点 10 的右子树却小于 10，这违反了 BST 定义。",
        "analysis_derivation": "区间边界传递破局：\n我们需要在递归时向下传递每个节点必须满足的**上限（upper）和下限（lower）值范围**。\n1. 初始化调用 `dfs(root, -inf, inf)`，根节点可以为任意值。\n2. 在递归的每一步中：\n   - 如果当前节点 `node` 为空，返回 `True`。\n   - 检查当前节点的值是否满足边界：`lower < node.val < upper`。若不满足，说明非法，返回 `False`。\n   - **向下更新边界**：\n     - 当向左子树递归时，所有左节点都必须小于当前节点。因此上限更新为当前节点的值：`dfs(node.left, lower, node.val)`。\n     - 当向右子树递归时，所有右节点都必须大于当前节点。因此下限更新为当前节点的值：`dfs(node.right, node.val, upper)`。\n   - 左右两边都合法才返回 `True`。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        \"\"\"
        时间复杂度: O(N) - 遍历所有节点一次
        空间复杂度: O(H) - 递归调用栈空间
        \"\"\"
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
"""
    },
    "69_kth_smallest_element_in_a_bst.py": {
        "title": "Kth Smallest Element in a BST (二叉搜索树中第 K 小的元素)",
        "difficulty": "Medium",
        "key_points": "二叉搜索树的中序遍历性质 / 栈迭代早期终止",
        "analysis_intuition": "直觉：BST（二叉搜索树）有一个非常关键的特性：**对 BST 进行中序遍历（左 -> 根 -> 右），得到的结果刚好是一个严格升序的序列**。所以，寻找第 k 小的元素，就是找出中序遍历中的第 k 个被访问节点。",
        "analysis_derivation": "为了提高性能并做到早期终止，我们可以使用**迭代版的中序遍历**（用一个显式栈模拟系统递归）：\n1. 初始化一个空栈 `stack`，当前指针 `curr = root`。\n2. 在 `curr` 不为空或栈不为空的条件中循环：\n   - **向左倾斜入栈**：一路将当前节点及其所有左侧后代全部压入栈中：`stack.append(curr); curr = curr.left`。这能确保我们总是优先探寻最小的节点。\n   - **出栈处理**：弹出栈顶元素，它就是当前中序遍历中最小的未访问节点。我们对计数器 `k` 减 1（`k -= 1`）。\n   - **早期终止**：如果 `k == 0`，说明找到了第 k 小的元素，直接返回该节点的值。\n   - **转向右子树**：令 `curr = popped_node.right`，准备处理右侧分支。\n由于使用迭代栈，我们一旦访问完第 k 个元素就立即退出，不会遍历整棵树，极佳地优化了时间复杂度。",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        \"\"\"
        时间复杂度: O(H + k) - H 是树的高度，需要一路向左压栈，然后向后迭代遍历 k 次
        空间复杂度: O(H) - 栈最大深度等于树的高度
        \"\"\"
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
"""
    },
    "70_lowest_common_ancestor_of_a_binary_search_tree.py": {
        "title": "Lowest Common Ancestor of a Binary Search Tree (二叉搜索树的最近公共祖先)",
        "difficulty": "Medium",
        "key_points": "BST 的大小偏序性质 / 树的自顶向下分岔",
        "analysis_intuition": "直觉：要在 BST 中找到两个节点 `p` 和 `q` 的最近公共祖先（LCA）。我们可以使用常规二叉树的后序遍历 LCA 算法，复杂度为 O(N)。但由于这是一棵二叉搜索树，我们完全可以利用数值大小关系进行快速的分治判定，把时间复杂度降低到 O(H)（在平衡树中为 O(log N)）。",
        "analysis_derivation": "BST 性质告诉我们：对于任何节点，其左子树的值都小于它，右子树的值都大于它。\n从根节点 `root` 开始自顶向下迭代检查：\n1. 如果 `p.val` 和 `q.val` 的值都小于当前 `root.val`，说明这两个目标节点一定都在当前节点的左子树中。我们将 `root` 移动到左孩子：`root = root.left`。\n2. 如果 `p.val` 和 `q.val` 的值都大于当前 `root.val`，说明它们一定都在当前节点的右子树中。我们将 `root` 移动到右孩子：`root = root.right`。\n3. **分岔点判定**：如果上面两个条件都不成立（即一个比 `root` 大，一个比 `root` 小；或者其中有一个就是当前 `root` 节点自己），说明在当前节点处，`p` 和 `q` 发生了“分道扬镳”。这个分岔点就是它们的最近公共祖先，直接返回 `root`。",
        "code": """class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        \"\"\"
        时间复杂度: O(H) - 沿着单条分支向下搜索，最坏为 O(N)，平衡树时为 O(log N)
        空间复杂度: O(1) - 仅需指针移动，无额外栈开销
        \"\"\"
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
"""
    },
    "71_implement_trie_prefix_tree.py": {
        "title": "Implement Trie (Prefix Tree) (实现 Trie (前缀树))",
        "difficulty": "Medium",
        "key_points": "前缀树设计 / 嵌套哈希结构",
        "analysis_intuition": "直觉：Trie 树（前缀树）是一种哈希树变体，常用于快速检索字符串前缀或进行自动补全。Trie 树的每个节点代表一个字符。根节点不包含字符，除根节点外每一个节点都仅包含一个字符；从根节点到某一个节点，路径上经过的字符连接起来就是该节点对应的字符串。",
        "analysis_derivation": "Trie 节点结构设计：\n我们可以将每个节点定义为一个字典 `children`，键（Key）为子字符，值（Value）为指向下一个 Trie 节点实例的指针。同时，使用一个布尔变量 `is_word` 记录当前节点是否是一个单词的结束标记。\n1. `insert(word)`：从根节点出发，遍历单词的每个字符 `char`。如果 `char` 不在当前节点的 `children` 字典中，就创建一个新的 Trie 节点加入其中。然后指针移动到该子节点。遍历完后，将最后一个节点的 `is_word` 设为 `True`。\n2. `search(word)`：沿着 `children` 指针向下检索单词的每一个字符，如果中途断掉则说明该单词不存在，返回 `False`；如果顺利到达结尾，返回最后一个节点的 `is_word` 状态。\n3. `startsWith(prefix)`：执行与 `search` 相同的检索过程。如果顺利走完前缀的所有字符，说明前缀存在（无需关注最后一个节点是否是单词结尾），返回 `True`；中途断掉则返回 `False`。",
        "code": """class TrieNode:
    def __init__(self):
        # 存储子节点映射 {字符: TrieNode}
        self.children = {}
        # 标记当前节点是否是单词的尾字符
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        \"\"\"插入一个单词
        时间复杂度: O(L) - L 为单词长度
        \"\"\"
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        \"\"\"查询单词是否存在
        时间复杂度: O(L)
        \"\"\"
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        \"\"\"查询是否存在以该前缀开头的单词
        时间复杂度: O(L)
        \"\"\"
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
"""
    },
    "72_add_and_search_word_data_structure_design.py": {
        "title": "Add and Search Word (添加与搜索单词 - 数据结构设计)",
        "difficulty": "Medium",
        "key_points": "前缀树 (Trie) + 带有通配符的递归 DFS 回溯",
        "analysis_intuition": "直觉：这道题是前缀树的进阶变体。我们需要设计一个单词查找系统，其中查找支持通配符 `'.'`（可以匹配任何单个字母）。如果不使用前缀树，随着添加单词的增加，大文本查询速度会严重变慢。使用前缀树后，我们可以利用 DFS 对通配符进行多路回溯查找。",
        "analysis_derivation": "1. 节点设计与常规 Trie 一致：包含字典 `children` 和布尔值 `is_word`。\n2. `addWord(word)`：常规前缀树插入操作，耗时 $O(L)$。\n3. `search(word)`：需要处理通配符 `'.'`。我们设计一个递归的 DFS 匹配函数 `dfs(node, i)`，表示当前在 Trie 的 `node` 节点，去尝试匹配单词 `word` 从第 `i` 个索引开始的子串：\n   - 如果 `i == len(word)`，返回当前节点的 `is_word` 标记。\n   - 取出当前要匹配的字符 `char = word[i]`：\n     - **通配符处理**：如果 `char == '.'`，说明它可以代表任何子字符。我们必须遍历当前节点 `node.children` 中的**所有子节点**进行分支尝试：只要其中任何一个子分支调用 `dfs(child, i + 1)` 返回 `True`，当前搜索就判定成功，返回 `True`。如果全部子分支都失败，返回 `False`。\n     - **普通字符处理**：如果 `char` 在 `node.children` 中，递归进入下一层：`dfs(node.children[char], i + 1)`。否则，直接返回 `False`。",
        "code": """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        \"\"\"添加单词
        时间复杂度: O(L)
        \"\"\"
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        \"\"\"检索单词（支持通配符 '.'）
        时间复杂度: 最坏为 O(M) - M 为字典中字符总数（通配符较多时深度搜索），通常为 O(L)
        \"\"\"
        def dfs(node, i):
            if i == len(word):
                return node.is_word
                
            char = word[i]
            if char == '.':
                # 通配符匹配：尝试遍历所有的子树分支
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # 常规字符匹配
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
                
        return dfs(self.root, 0)
"""
    },
    "73_word_search_ii.py": {
        "title": "Word Search II (单词搜索 Ⅱ)",
        "difficulty": "Hard",
        "key_points": "前缀树 (Trie) + 二维网格回溯 (Backtracking DFS) + 剪枝优化",
        "analysis_intuition": "直觉：本题是“单词搜索 I”的升级版。如果对于 `words` 列表中的每个单词都分别在网格里运行一遍回溯 DFS，时间复杂度是 O(W * M * N * 3^L)（W 是单词数量），会严重超时。我们需要一次性在网格中搜索所有的单词。",
        "analysis_derivation": "前缀树加速网格回溯与剪枝破局：\n与其对单词列表进行外层迭代，不如**将所有待检索的单词构建到一棵前缀树 (Trie) 中**，然后我们在网格的每个位置启动 DFS 搜索时，**让网格的移动与 Trie 树的指针移动同步进行**。\n1. **建树**：将 `words` 写入 Trie 树。为了方便，我们在单词结尾的节点上直接保存该单词的值（如 `node.word = word`），这样一旦在搜索中匹配到单词节点，可以直接获取到完整的单词。\n2. **网格 DFS**：在位置 `(r, c)`：\n   - 如果当前网格字符 `char` 在当前 Trie 节点 `node.children` 中，说明这是一条有潜力的匹配路径。我们移动到 `child_node = node.children[char]`。\n   - 检查 `child_node`：如果它包含 `word` 属性，说明我们找到了一个有效的单词，加入结果集中。**重要优化：立即将 `child_node.word` 设为 `None`，防止同一个单词在不同网格位置被重复搜出来加入结果集。**\n   - 原地标记当前格子已被访问（如 `board[r][c] = '#'`），然后向四周递归继续搜索。\n   - 回溯恢复现场（`board[r][c] = char`）。\n3. **高阶剪枝优化**：当一个叶子节点的单词被找到后，或者一个节点的所有子树都为空时，说明这部分的 Trie 树枝已经没有利用价值了。我们可以在回溯时**就地将该无效子节点从父节点的 children 字典中删除**（剪枝）。这可以极大防止冗余的重复路径探索，是能通过力扣超强测试用例的关键。",
        "code": """from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 存储匹配成功的完整单词

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        \"\"\"
        时间复杂度: O(M * N * 4 * 3^(L-1)) - M, N 为网格边长，L 为单词最大长度
        空间复杂度: O(W * L) - Trie 树占用的存储空间，W 为单词数，L 为最大长度
        \"\"\"
        # 1. 构建前缀树
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
            
        m, n = len(board), len(board[0])
        res = []
        
        # 2. 网格回溯 DFS 函数
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]
            
            # 如果匹配成功一个单词，将其加入结果
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # 防止重复添加
                
            # 临时标记已访问
            board[r][c] = '#'
            
            # 探索四周邻居
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_char = board[nr][nc]
                    if next_char in curr_node.children:
                        dfs(nr, nc, curr_node)
                        
            # 回溯恢复现场
            board[r][c] = char
            
            # 高阶剪枝优化：如果当前节点没有子节点了，从父节点中删除它
            if not curr_node.children:
                parent_node.children.pop(char)
                
        # 3. 遍历网格每个格子作为起点尝试搜索
        for r in range(m):
            for c in range(n):
                start_char = board[r][c]
                if start_char in root.children:
                    dfs(r, c, root)
                    
        return res
"""
    }
}
