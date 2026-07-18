from typing import List, Optional, Dict, Set

# Graph Valid Tree (以图判树) - Medium
# 🔑 核心考点: 无向图环路检测 / 连通性校验 / 并查集 (Union Find)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：一棵树本质上是一个**无环且连通**的无向图。在图论中，一个含有 `n` 个节点的图如果是一棵树，它必须满足两个核心条件：1. 边数刚好是 `n - 1`。 2. 图中没有任何环路（或者所有节点都是连通的）。
#   - 思维推导: 
#     使用并查集 (Union Find) 来高效判断：
#     1. 如果边的数量 `len(edges) != n - 1`，则直接判定不可能是树，返回 `False`。
#     2. 初始化并查集。遍历所有的边 `(u, v)`，尝试在并查集中将 `u` 和 `v` 的集合合并：
#        - 如果合并前发现 `find(u) == find(v)`，说明 `u` 和 `v` 已经在同一个连通块中了，此时再加上这条边必然会在无向图中形成环。因此直接判定不是树，返回 `False`。
#        - 否则，合并两个连通块。
#     3. 因为我们已经做过了边数 `len(edges) == n - 1` 的前置检查，且确认没有环，所以该图必然也是完全连通的。返回 `True` 即可。并查集的平均操作复杂度接近 O(1)。

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        时间复杂度: O(N * alpha(N)) - alpha 是阿克曼函数的反函数，可视为常数 O(1)
        空间复杂度: O(N) - 并查集的 parent 数组
        """
        # 树的必要条件：边数必须为节点数 - 1
        if len(edges) != n - 1:
            return False
            
        parent = [i for i in range(n)]
        
        def find(i):
            if parent[i] == i:
                return i
            # 路径压缩优化
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False  # 已经在同一个集合中，说明有环
            parent[root_i] = root_j
            return True
            
        for u, v in edges:
            if not union(u, v):
                return False  # 检测到环路
                
        return True

