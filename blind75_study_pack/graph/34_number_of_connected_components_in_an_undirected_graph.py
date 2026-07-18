from typing import List, Optional, Dict, Set

# Number of Connected Components in an Undirected Graph (无向图中连通分量的数目) - Medium
# 🔑 核心考点: 无向图遍历 / 并查集 (Union Find)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：给定一个无向图和它的所有边，我们需要找出有多少个互不连通的子图。我们可以用 DFS/BFS 遍历整个图，每开始一次遍历就代表找到了一个连通分量。但最简练的做法是使用并查集。
#   - 思维推导: 
#     1. 初始状态下，我们假设图中有 `n` 个独立的节点，即连通分量初始数量为 `count = n`。
#     2. 遍历所有的边 `(u, v)`：
#        - 通过并查集的 `find` 操作找到 `u` 和 `v` 的根节点。
#        - 如果它们的根节点不同，说明这两个原本独立的连通块之间有一条边相连。我们使用 `union` 操作将这两个连通块合并为一体，同时连通分量数 `count` 减 1。
#        - 如果根节点相同，说明它们原本就已经连通，不需要做任何改动。
#     3. 遍历完所有的边之后，最后的 `count` 值即为无向图中连通分量的总数。

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        时间复杂度: O(N + E * alpha(N)) - N 为节点数，E 为边数，均摊复杂度接近 O(N + E)
        空间复杂度: O(N) - 并查集 parent 数组
        """
        parent = [i for i in range(n)]
        count = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # 路径压缩
            return parent[i]
            
        def union(i, j):
            nonlocal count
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                count -= 1  # 成功合并两个原本不连通的部分，连通分量数减 1
                
        for u, v in edges:
            union(u, v)
            
        return count

