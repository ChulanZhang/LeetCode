from typing import List, Optional, Dict, Set

# Course Schedule (课程表) - Medium
# 🔑 核心考点: 有向图拓扑排序 (Topological Sort) - Kahn 算法 (BFS) / DFS 环路检测
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：先修课程的关系构成了一个有向图。如果课程 `A` 是 `B` 的先修课，就有一条从 `A` 指向 `B` 的有向边。如果我们想修完所有课程，这个有向图中绝对不能存在环路（比如 A 是 B 的先修课，B 是 C 的先修课，C 又是 A 的先修课）。
#   - 思维推导: 
#     检测有向图是否存在环路的经典方法是**拓扑排序**。我们采用基于广度优先搜索 (BFS) 的 Kahn 算法：
#     1. 统计每个节点的入度（指向该节点的边数）和构建邻接表。
#     2. 将所有入度为 0 的节点（即没有先修课程要求的课程）放入队列。
#     3. 当队列不为空时，弹出队列首部的节点，将其加入已修课程，并遍历它的所有邻居节点（受它制约的后续课程）。对于每个邻居，将其入度减 1。如果减 1 后邻居的入度变为 0，则将该邻居加入队列。
#     4. 最后，检查已修课程的数量是否等于课程总数 `numCourses`。如果等于，说明拓扑排序成功，无环；否则，说明图中存在环，无法修完。

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        时间复杂度: O(V + E) - V 为课程数，E 为先修关系数
        空间复杂度: O(V + E) - 存储邻接表与入度数组
        """
        # 构建邻接表与入度表
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
            
        # 入度为 0 的课程入队
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited_count = 0
        
        while queue:
            curr = queue.popleft()
            visited_count += 1
            
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return visited_count == numCourses

