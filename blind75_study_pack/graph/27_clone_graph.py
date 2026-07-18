from typing import List, Optional, Dict, Set

# Clone Graph (克隆图) - Medium
# 🔑 核心考点: 图的遍历 - 深度优先搜索 (DFS) / 广度优先搜索 (BFS) + 哈希表映射
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：克隆一个图，我们需要遍历原图的所有节点。但是原图可能存在环（Cycle），所以如果不记录已经克隆过的节点，遍历就会陷入无限死循环。
#   - 思维推导: 
#     我们需要使用一个哈希表 `cloned` 来建立原节点到新克隆节点的映射（`old_node -> new_node`）。
#     每次遇到一个节点：
#     1. 如果这个节点已经存在于 `cloned` 中，直接返回对应的克隆节点。
#     2. 如果不在，说明它是第一次被访问。我们实例化一个值相同的新节点，并存入 `cloned` 中。
#     3. 然后，我们遍历原节点的邻居列表 `neighbors`，递归地克隆每一个邻居，并将克隆后的邻居节点添加到新节点的邻居列表中。
#     这种 DFS 配合哈希表映射的模式可以确保图的每一个节点和每一条边都被精确复制且不发生死循环。

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        时间复杂度: O(V + E) - 每个节点和每条边各访问一次
        空间复杂度: O(V) - 递归调用栈与哈希表占用的空间
        """
        if not node:
            return None
            
        cloned = {}
        
        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
                
            # 复制当前节点，并存入映射表以防环路死循环
            copy = Node(curr.val)
            cloned[curr] = copy
            
            # 递归复制所有的邻居节点
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)

