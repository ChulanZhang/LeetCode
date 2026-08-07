# Tree category data
PROBLEMS = {
    "60_maximum_depth_of_binary_tree.py": {
        "title": "Maximum Depth of Binary Tree",
        "difficulty": "Easy",
        "key_points": "Binary Tree Recursion - Depth-First Search (DFS)",
        "analysis_intuition": "The maximum depth of a binary tree is the maximum of the depths of its left and right subtrees, plus 1 for the root node itself.",
        "analysis_derivation": "We can express this relation recursively:\n1. **Base case**: If `root` is null, the subtree is empty, so return height 0.\n2. **Recursion**: Recursively calculate the maximum depth of the left subtree `left_depth` and the right subtree `right_depth`.\n3. **Combine**: The result is `max(left_depth, right_depth) + 1`.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(N) - Each node is visited exactly once
        # Space Complexity: O(H) - H is the height of the tree, representing the recursion stack depth
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""
    },
    "61_same_tree.py": {
        "title": "Same Tree",
        "difficulty": "Easy",
        "key_points": "Binary Tree - Synchronous Recursion",
        "analysis_intuition": "For two trees to be identical, their root values must be equal, and their left subtrees must be identical, and their right subtrees must be identical. We can compare them using synchronous recursion.",
        "analysis_derivation": "Compare two nodes `p` and `q` simultaneously:\n1. If both `p` and `q` are null, we reached the leaf ends simultaneously with matching structures, return True.\n2. If only one is null, or their values differ (`p.val != q.val`), they are not identical, return False.\n3. Otherwise, recursively verify that the left subtrees match `self.isSameTree(p.left, q.left)` and the right subtrees match `self.isSameTree(p.right, q.right)`. Both must be True.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity: O(N) - N is the smaller number of nodes in p and q
        # Space Complexity: O(H) - Recursion stack space
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
        # Check left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
"""
    },
    "62_invert_binary_tree.py": {
        "title": "Invert Binary Tree",
        "difficulty": "Easy",
        "key_points": "Binary Tree - In-Place Node Swapping",
        "analysis_intuition": "Inverting a binary tree (mirroring it) means swapping the left child and right child of every node in the tree recursively.",
        "analysis_derivation": "1. **Base case**: If the current node `root` is null, return `None`.\n2. **Swap children**: Swap the left and right pointers of the current node using a parallel assignment: `root.left, root.right = root.right, root.left`.\n3. **Recursive step**: Recursively invert the left subtree `self.invertTree(root.left)` and the right subtree `self.invertTree(root.right)`.\n4. Return the mutated `root` node.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time Complexity: O(N) - Visit every node once
        # Space Complexity: O(H) - Recursion stack space
        if not root:
            return None
            
        # Swap the left and right child pointers
        root.left, root.right = root.right, root.left
        
        # Recursively invert the children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
"""
    },
    "63_binary_tree_maximum_path_sum.py": {
        "title": "Binary Tree Maximum Path Sum",
        "difficulty": "Hard",
        "key_points": "Post-Order DFS / Path Contribution Merging",
        "analysis_intuition": "A path in a binary tree can 'bend' at a node, meaning it can travel from the left subtree, through the node, and into the right subtree. For any node, the maximum sum of a path bending at this node is `node.val + left_gain + right_gain`. However, a path with a bend cannot be extended upward to a parent node because binary tree paths cannot have branches.",
        "analysis_derivation": "Post-Order DFS Mechanism:\n1. Maintain a global variable `max_sum` to store the maximum path sum found, initialized to negative infinity.\n2. Define a DFS helper that returns the **maximum single-path contribution** the subtree can provide to its parent (i.e. we must choose only *one* branch to extend upward):\n   - If the node is null, return 0.\n   - Calculate the max gain from the left child: `left = max(0, dfs(node.left))`. If a child's gain is negative, we discard it (greedy choice).\n   - Calculate the max gain from the right child: `right = max(0, dfs(node.right))`.\n   - **Calculate the bent path**: The max path sum bending at the current node is `node.val + left + right`. Update `max_sum` with this value.\n   - **Return single-path gain**: Return `node.val + max(left, right)` to the parent node since the path cannot branch.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(N) - Each node is visited exactly once during DFS
        # Space Complexity: O(H) - Auxiliary recursion stack space
        max_sum = float('-inf')
        
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
                
            # Compute maximum single-path gain from left and right children (ignore negative gains)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Update the global maximum path sum considering a path that splits at the current node
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)
            
            # Return the maximum single-path gain (cannot take both left and right to the parent)
            return node.val + max(left_gain, right_gain)
            
        dfs(root)
        return max_sum
"""
    },
    "64_binary_tree_level_order_traversal.py": {
        "title": "Binary Tree Level Order Traversal",
        "difficulty": "Medium",
        "key_points": "Breadth-First Search (BFS) / Queue Level Splitting",
        "analysis_intuition": "To output nodes level by level, we use a Breadth-First Search (BFS) facilitated by a queue. When processing a level, we must determine the size of the queue at the start of the level. This allows us to process exactly the nodes belonging to the current level before moving to the next.",
        "analysis_derivation": "1. If `root` is null, return an empty list `[]`.\n2. Initialize a double-ended queue `queue` containing the `root`.\n3. While the queue is not empty:\n   - Get the number of nodes in the current level: `level_size = len(queue)`.\n   - Iterate `level_size` times. Dequeue a node, append its value to the current level's list `level_nodes`, and enqueue its non-null left and right children.\n   - Append `level_nodes` to the global result list.",
        "code": """from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time Complexity: O(N) - Visit every node once
        # Space Complexity: O(N) - Queue holds at most N/2 nodes at the bottom level
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                current_level.append(curr.val)
                # Enqueue children for the next level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(current_level)
            
        return res
"""
    },
    "65_serialize_and_deserialize_binary_tree.py": {
        "title": "Serialize and Deserialize Binary Tree",
        "difficulty": "Hard",
        "key_points": "Pre-Order DFS / Tree Splicing / Serialization Protocol",
        "analysis_intuition": "To serialize a binary tree into a string and deserialize it back, the serialized string must store the structure (including null nodes) explicitly. A traversal string without null markers cannot uniquely reconstruct a binary tree.",
        "analysis_derivation": "Pre-Order DFS (Root -> Left -> Right) Protocol:\n1. **Serialize**:\n   - Run pre-order DFS on the tree. If a node is null, append a placeholder like `'#'` or `'N'` to the result.\n   - If the node is not null, append its value followed by a delimiter (like `','`).\n   - Example: A tree is serialized to `'1,2,#,#,3,4,#,#,5,#,#'`.\n2. **Deserialize**:\n   - Split the serialized string by `','` and convert it into a queue `queue`.\n   - Define a recursive helper `dfs(queue)` that dequeues the first element:\n     - If it is `'#'`, return `None`.\n     - Otherwise, instantiate `node = TreeNode(int(val))`.\n     - Recursively construct the left child: `node.left = dfs()`.\n     - Recursively construct the right child: `node.right = dfs()`.\n     - Return `node`.",
        "code": """from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        # Encodes a tree to a single string.
        # Time Complexity: O(N)
        # Space Complexity: O(N)
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
        # Decodes your encoded data to tree.
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        vals = deque(data.split(','))
        
        def dfs():
            val = vals.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            # Construct subtrees in pre-order sequence
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()
"""
    },
    "66_subtree_of_another_tree.py": {
        "title": "Subtree of Another Tree",
        "difficulty": "Easy",
        "key_points": "Binary Tree Recursion - Substructure Matching",
        "analysis_intuition": "To check if `subRoot` is a subtree of `root`, three cases are possible: 1. `root` and `subRoot` are identical trees. 2. `subRoot` is a subtree of `root.left`. 3. `subRoot` is a subtree of `root.right`.",
        "analysis_derivation": "1. Helper `isSameTree(p, q)`: Returns True if two trees have identical structures and values.\n2. Main function `isSubtree(root, subRoot)`:\n   - If `root` is null, we reached the end of the search path without finding a match. Return False (since `subRoot` is non-empty).\n   - Check `isSameTree(root, subRoot)`. If True, return True.\n   - Otherwise, recursively search in the child nodes: `self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time Complexity: O(M * N) - M, N are node counts. Worst case checks isSame for all root nodes
        # Space Complexity: O(H) - H is height of the root tree (recursion stack depth)
        if not root:
            return False
            
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
            
        # Check if identical at current root, otherwise recurse left and right
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
"""
    },
    "67_construct_binary_tree_from_preorder_and_inorder_traversal.py": {
        "title": "Construct Binary Tree from Preorder and Inorder Traversal",
        "difficulty": "Medium",
        "key_points": "Pre-Order & In-Order Properties / Divide and Conquer / Index Mapping",
        "analysis_intuition": "In a pre-order traversal, the first element is always the **root node** of the current tree/subtree. In an in-order traversal, the root node partitions the elements into the left subtree (all elements to the left of the root) and the right subtree (all elements to the right). We can use this property to recursively rebuild the tree.",
        "analysis_derivation": "1. **Root Extraction**: The first element in preorder is the root value: `root_val = preorder[pre_start]`. Instantiate `root = TreeNode(root_val)`.\n2. **Partitioning**: Locate the index of `root_val` in inorder, say `mid`. The elements to the left of `mid` represent the left subtree, and elements to the right represent the right subtree.\n3. **Subproblem division**: The left subtree has size `left_size = mid - in_start`. Thus, the left subtree's preorder values are located at indices `[pre_start + 1 ... pre_start + left_size]`, and the right subtree's preorder values are at indices `[pre_start + left_size + 1 ... pre_end]`.\n4. **Optimization**: Slicing arrays in recursion takes O(N^2) time. We optimize this to O(N) by storing inorder values in a hash map (`inorder_map = {val: idx}`) for O(1) index lookup and passing boundary pointers in recursion.",
        "code": """from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time Complexity: O(N) - N is the number of nodes. Hash map index lookup is O(1)
        # Space Complexity: O(N) - Hash map storage and recursion call stack
        
        # Cache inorder indices to avoid O(N) searches during recursion
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
                
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Locate root in inorder list
            mid = inorder_map[root_val]
            left_size = mid - in_start  # Number of nodes in left subtree
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            root.right = build(pre_start + left_size + 1, pre_end, mid + 1, in_end)
            
            return root
            
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
"""
    },
    "68_validate_binary_search_tree.py": {
        "title": "Validate Binary Search Tree",
        "difficulty": "Medium",
        "key_points": "BST Definition - Interval Bounds DFS Propagation",
        "analysis_intuition": "A common mistake is validating only that a node is greater than its left child and smaller than its right child. This is incorrect. In a Binary Search Tree (BST), **all nodes in the left subtree must be less than the parent node, and all nodes in the right subtree must be greater than the parent node**.",
        "analysis_derivation": "To enforce this definition globally, we propagate valid open intervals `(lower, upper)` down during DFS:\n1. Initialize `validate(root, -inf, inf)`.\n2. In each step:\n   - If the node is null, return True.\n   - Verify if the node's value falls inside the open interval: `lower < node.val < upper`. If not, return False.\n   - **Update bounds for children**:\n     - When validating the left child, its value must be less than the current node's value. The upper bound shifts to `node.val`: `validate(node.left, lower, node.val)`.\n     - When validating the right child, its value must be greater than the current node's value. The lower bound shifts to `node.val`: `validate(node.right, node.val, upper)`.\n   - Return True if both children are valid BSTs.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity: O(N) - Visit every node once
        # Space Complexity: O(H) - Recursion stack space
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
                
            # Node value must be strictly within the allowed range
            if not (lower < node.val < upper):
                return False
                
            # Left child values must be in (lower, node.val); right child values in (node.val, upper)
            return (validate(node.left, lower, node.val) and 
                    validate(node.right, node.val, upper))
                    
        return validate(root)
"""
    },
    "69_kth_smallest_element_in_a_bst.py": {
        "title": "Kth Smallest Element in a BST",
        "difficulty": "Medium",
        "key_points": "BST In-Order Traversal Properties / Iterative Stack with Early Termination",
        "analysis_intuition": "An in-order traversal (Left -> Root -> Right) of a Binary Search Tree (BST) visits nodes in strictly ascending order. Thus, finding the k-th smallest element is equivalent to finding the k-th node visited during an in-order traversal.",
        "analysis_derivation": "To optimize performance, we use an **iterative in-order traversal** utilizing an explicit stack. This allows us to stop the traversal immediately once the k-th element is reached:\n1. Initialize an empty stack and set `curr = root`.\n2. In a loop while `curr` is not null or the stack is not empty:\n   - **Go left**: Push the current node and all its left descendants onto the stack: `stack.append(curr); curr = curr.left`. This ensures we always process the smallest element next.\n   - **Pop and process**: Pop from the stack. This is the next smallest element in in-order. Decrement `k` by 1.\n   - **Check target**: If `k == 0`, we have found the k-th smallest element. Return its value immediately.\n   - **Go right**: Set `curr = popped_node.right` to process its right subtree.",
        "code": """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time Complexity: O(H + k) - H is the height of the tree. We traverse down to the leftmost leaf, then perform k pop operations
        # Space Complexity: O(H) - Stack stores at most H nodes
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Travel to the leftmost node, pushing all nodes along the path to the stack
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # 2. Process the top of the stack (smallest unvisited node)
            curr = stack.pop()
            k -= 1
            
            # 3. If we've popped k elements, we have found the target
            if k == 0:
                return curr.val
                
            # 4. Move to the right child
            curr = curr.right
            
        return -1
"""
    },
    "70_lowest_common_ancestor_of_a_binary_search_tree.py": {
        "title": "Lowest Common Ancestor of a Binary Search Tree",
        "difficulty": "Medium",
        "key_points": "BST Partial Order / Binary Search-like Node Splitting",
        "analysis_intuition": "Finding the Lowest Common Ancestor (LCA) in a general binary tree takes O(N) time and O(H) space. However, because this is a Binary Search Tree (BST), we can use the value ordering property to find the LCA in O(H) time and O(1) space.",
        "analysis_derivation": "In a BST, a node's left child has a smaller value and its right child has a larger value.\nTraverse starting from the `root`:\n1. If both `p.val` and `q.val` are less than the current node's value, the LCA must reside in the left subtree. Move left: `curr = curr.left`.\n2. If both `p.val` and `q.val` are greater than the current node's value, the LCA must reside in the right subtree. Move right: `curr = curr.right`.\n3. **Split Point**: If neither condition is met (one value is larger and the other is smaller, or one value equals the current node's value), the paths to `p` and `q` split here. The current node is the LCA. Return it.",
        "code": """class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time Complexity: O(H) - We traverse down a single branch of the tree. H is O(log N) for balanced trees
        # Space Complexity: O(1) - Constant auxiliary space
        curr = root
        
        while curr:
            # If both targets are in the left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If both targets are in the right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                # Split point found (or current is one of p or q)
                return curr
                
        return None
"""
    },
    "71_implement_trie_prefix_tree.py": {
        "title": "Implement Trie (Prefix Tree)",
        "difficulty": "Medium",
        "key_points": "Trie Structure / Nested Dictionaries",
        "analysis_intuition": "A Trie (Prefix Tree) is a tree structure used for fast string retrieval and autocomplete queries. Each node in the Trie represents a character. A path from the root to a node spells out a word.",
        "analysis_derivation": "Trie Node Structure Design:\nWe can implement a Trie node using a dictionary `children` mapping characters to child `TrieNode` objects, and a boolean flag `is_word` indicating if the node marks the end of a complete word.\n1. `insert(word)`: Iterate through the word's characters. If a character is not in the current node's `children`, insert a new `TrieNode`. Move the pointer to the child node. At the end of the word, set `is_word = True`.\n2. `search(word)`: Traverse the Trie following the word's characters. If a character is missing, return False. At the end, return `is_word` (which must be True for the word to exist).\n3. `startsWith(prefix)`: Traverse the Trie following the prefix. If the traversal succeeds, the prefix exists. Return True.",
        "code": """class TrieNode:
    def __init__(self):
        # Map of children nodes {char: TrieNode}
        self.children = {}
        # Boolean to check if node marks the end of a word
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Time Complexity: O(L) - L is word length
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Time Complexity: O(L)
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        # Time Complexity: O(L)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
"""
    },
    "72_add_and_search_word_data_structure_design.py": {
        "title": "Add and Search Word",
        "difficulty": "Medium",
        "key_points": "Trie + Wildcard DFS Backtracking",
        "analysis_intuition": "This problem adds wildcard searches to the standard Trie, where `'.'` can match any single character. While adding words is identical to insertion in a Trie, searching requires a DFS-based backtracking approach to handle the `'.'` character.",
        "analysis_derivation": "1. Node structure: Standard Trie node (`children` dict, `is_word` boolean).\n2. `addWord(word)`: Standard Trie word insertion.\n3. `search(word)`: Define a recursive helper `dfs(node, i)` that checks matching starting from character index `i` of `word` at Trie node `node`:\n   - If `i == len(word)`, return `node.is_word`.\n   - Let `char = word[i]`:\n     - **Wildcard dot**: If `char == '.'`, we must try all branches in `node.children.values()`. If any branch returns True for `dfs(child, i + 1)`, search is successful. Return True. If all fail, return False.\n     - **Standard character**: If `char` exists in `node.children`, recursively check the child: `dfs(node.children[char], i + 1)`. Otherwise, return False.",
        "code": """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Time Complexity: O(L) - L is word length
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Time Complexity: O(M) worst case - M is total nodes in the Trie (wildcard search), usually O(L)
        def dfs(node, i):
            if i == len(word):
                return node.is_word
                
            char = word[i]
            if char == '.':
                # Wildcard search: try all possible child paths
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # Direct character match
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
                
        return dfs(self.root, 0)
"""
    },
    "73_word_search_ii.py": {
        "title": "Word Search II",
        "difficulty": "Hard",
        "key_points": "Trie + Grid DFS Backtracking + Node Deletion Pruning",
        "analysis_intuition": "This is Word Search I with a list of words. Searching for each word individually takes O(W * M * N * 3^L) time (where W is word count), which will time out. We must search for all words in a single grid scan.",
        "analysis_derivation": "Trie-Accelerated Grid DFS Backtracking:\nInstead of looping through words, we **store all target words in a Trie**. During the grid DFS traversal, we synchronize the grid position shifts with navigation in the Trie.\n1. **Trie building**: Insert all words into the Trie. For convenience, store the actual word string at its leaf node: `node.word = word`.\n2. **Grid DFS**: At `(r, c)`:\n   - If `board[r][c] = char` is in the Trie node's children, move to `child_node = node.children[char]`.\n   - If `child_node` has a `word` attribute, we found a match. Add it to results and **immediately clear `child_node.word = None` to prevent duplicate matches**.\n   - Mark the grid cell as visited (`board[r][c] = '#'`), recursively call DFS in 4 directions, then restore the cell's character (backtrack).\n3. **Trie Pruning Optimization**: If a node has no children (`not curr_node.children`), it is a dead end. We can delete it from its parent's `children` map on backtracking. This pruning prevents exploring redundant grid paths and is crucial to passing strict constraints.",
        "code": """from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word if the node marks a word's end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time Complexity: O(M * N * 4 * 3^(L-1)) - M, N are board dimensions, L is maximum word length
        # Space Complexity: O(W * L) - Space to store words in the Trie
        
        # 1. Build the Trie
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
        
        # 2. Backtracking DFS
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]
            
            # Match found, record word and clear to prevent duplicate matches
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None
                
            # Temporarily mark grid cell as visited
            board[r][c] = '#'
            
            # Explore 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_char = board[nr][nc]
                    if next_char in curr_node.children:
                        dfs(nr, nc, curr_node)
                        
            # Restore grid cell (Backtrack)
            board[r][c] = char
            
            # Trie Pruning: Remove leaf nodes with no children
            if not curr_node.children:
                parent_node.children.pop(char)
                
        # 3. Scan the grid and trigger DFS from matching start characters
        for r in range(m):
            for c in range(n):
                start_char = board[r][c]
                if start_char in root.children:
                    dfs(r, c, root)
                    
        return res
"""
    }
}
