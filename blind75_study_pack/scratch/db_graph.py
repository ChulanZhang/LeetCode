# Graph category data
PROBLEMS = {
    "27_clone_graph.py": {
        "title": "Clone Graph (克隆图)",
        "difficulty": "Medium",
        "key_points": "图的遍历 - 深度优先搜索 (DFS) / 广度优先搜索 (BFS) + 哈希表映射",
        "analysis_intuition": "直觉：克隆一个图，我们需要遍历原图的所有节点。但是原图可能存在环（Cycle），所以如果不记录已经克隆过的节点，遍历就会陷入无限死循环。",
        "analysis_derivation": "我们需要使用一个哈希表 `cloned` 来建立原节点到新克隆节点的映射（`old_node -> new_node`）。\n每次遇到一个节点：\n1. 如果这个节点已经存在于 `cloned` 中，直接返回对应的克隆节点。\n2. 如果不在，说明它是第一次被访问。我们实例化一个值相同的新节点，并存入 `cloned` 中。\n3. 然后，我们遍历原节点的邻居列表 `neighbors`，递归地克隆每一个邻居，并将克隆后的邻居节点添加到新节点的邻居列表中。\n这种 DFS 配合哈希表映射的模式可以确保图的每一个节点和每一条边都被精确复制且不发生死循环。",
        "code": """class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        \"\"\"
        时间复杂度: O(V + E) - 每个节点和每条边各访问一次
        空间复杂度: O(V) - 递归调用栈与哈希表占用的空间
        \"\"\"
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
"""
    },
    "28_course_schedule.py": {
        "title": "Course Schedule (课程表)",
        "difficulty": "Medium",
        "key_points": "有向图拓扑排序 (Topological Sort) - Kahn 算法 (BFS) / DFS 环路检测",
        "analysis_intuition": "直觉：先修课程的关系构成了一个有向图。如果课程 `A` 是 `B` 的先修课，就有一条从 `A` 指向 `B` 的有向边。如果我们想修完所有课程，这个有向图中绝对不能存在环路（比如 A 是 B 的先修课，B 是 C 的先修课，C 又是 A 的先修课）。",
        "analysis_derivation": "检测有向图是否存在环路的经典方法是**拓扑排序**。我们采用基于广度优先搜索 (BFS) 的 Kahn 算法：\n1. 统计每个节点的入度（指向该节点的边数）和构建邻接表。\n2. 将所有入度为 0 的节点（即没有先修课程要求的课程）放入队列。\n3. 当队列不为空时，弹出队列首部的节点，将其加入已修课程，并遍历它的所有邻居节点（受它制约的后续课程）。对于每个邻居，将其入度减 1。如果减 1 后邻居的入度变为 0，则将该邻居加入队列。\n4. 最后，检查已修课程的数量是否等于课程总数 `numCourses`。如果等于，说明拓扑排序成功，无环；否则，说明图中存在环，无法修完。",
        "code": """from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        \"\"\"
        时间复杂度: O(V + E) - V 为课程数，E 为先修关系数
        空间复杂度: O(V + E) - 存储邻接表与入度数组
        \"\"\"
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
"""
    },
    "29_pacific_atlantic_water_flow.py": {
        "title": "Pacific Atlantic Water Flow (太平洋大西洋水流问题)",
        "difficulty": "Medium",
        "key_points": "多源深度优先搜索 (DFS) / 逆向遍历",
        "analysis_intuition": "直觉：我们要找出哪些格子既能流向太平洋（网格左侧和上方），又能流向大西洋（网格右侧和下方）。如果对每个格子分别运行一遍搜索，时间复杂度将是 O((M * N)^2)，会超时。",
        "analysis_derivation": "逆向思维破局：\n与其从网格的每个点“向下流”寻找海洋，不如**从太平洋和大西洋的边界“向上爬”**（逆水流方向移动，水流是从高往低，所以逆向就是从低往高，只能走到高度大于或等于当前格子的相邻格）。\n1. 我们声明两个布尔矩阵 `pacific_reach` 和 `atlantic_reach`，记录从对应的洋边界出发可以逆向到达的所有网格位置。\n2. 从太平洋的边界（第一行和第一列）出发运行 DFS，标记所有可达的位置。\n3. 从大西洋的边界（最后一行和最后一列）出发运行 DFS，标记所有可达的位置。\n4. 遍历整个网格，若某个格子在两个布尔矩阵中均为 `True`，说明它既能流向太平洋也能流向大西洋，加入结果集。时间复杂度大幅降低为 O(M * N)。",
        "code": """from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        \"\"\"
        时间复杂度: O(m * n) - 每个格子最多被 DFS 访问常数次
        空间复杂度: O(m * n) - 存储可达状态矩阵与调用栈
        \"\"\"
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reach = [[False] * n for _ in range(m)]
        atlantic_reach = [[False] * n for _ in range(m)]
        
        def dfs(r, c, reach, prev_height):
            # 边界检查、是否访问过、以及是否满足逆水流方向（新高度必须大于或等于旧高度）
            if (r < 0 or r >= m or c < 0 or c >= n or 
                reach[r][c] or heights[r][c] < prev_height):
                return
            reach[r][c] = True
            
            # 向四个方向扩散
            dfs(r + 1, c, reach, heights[r][c])
            dfs(r - 1, c, reach, heights[r][c])
            dfs(r, c + 1, reach, heights[r][c])
            dfs(r, c - 1, reach, heights[r][c])
            
        # 从太平洋（第一行/第一列）和大西洋（最后一行/最后一列）的边界出发进行逆向 DFS
        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, n - 1, atlantic_reach, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(m - 1, j, atlantic_reach, heights[m - 1][j])
            
        # 筛选出既能到达太平洋也能到达大西洋的网格坐标
        res = []
        for r in range(m):
            for c in range(n):
                if pacific_reach[r][c] and atlantic_reach[r][c]:
                    res.append([r, c])
        return res
"""
    },
    "30_number_of_islands.py": {
        "title": "Number of Islands (岛屿数量)",
        "difficulty": "Medium",
        "key_points": "网格遍历 - 深度优先搜索 (DFS) / 广度优先搜索 (BFS) / 并查集 (Union Find)",
        "analysis_intuition": "直觉：我们需要寻找被 '0'（水）包围的 '1'（陆地）组成的连通块的数量。这可以通过遍历网格来完成。当我们遇到一个 '1' 时，就代表找到了一个新岛屿，此时我们需要把与这个陆地相连的所有陆地都标记为已访问，避免重复计数。",
        "analysis_derivation": "1. 遍历二维网格的每一个格子 `(r, c)`。\n2. 如果 `grid[r][c] == '1'`：\n   - 岛屿计数器加 1。\n   - 启动 DFS 搜索：从当前格子出发，向上下左右四个方向扩散。一旦遇到相邻的 `'1'`，将其修改为 `'0'`（原地标记为已访问，这是一种常见的空间优化手段，避免使用 `visited` 集合）。\n   - DFS 扩散结束后，与该陆地连通的所有陆地都被沉没成了 `'0'`。\n3. 继续遍历网格，后续遇到的 `'1'` 一定是新的独立岛屿。",
        "code": """from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        \"\"\"
        时间复杂度: O(m * n) - 每个格子最多被访问常数次
        空间复杂度: O(m * n) - 最坏情况下（网格全为陆地）DFS 的递归调用栈深度
        \"\"\"
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # 越界检查或遇到水 '0' 则停止扩散
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            # 原地淹没陆地，防止重复访问
            grid[r][c] = '0'
            # 递归向四周扩散
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    # 发现新岛屿，启动 DFS 将其全部连通区域标记为水
                    island_count += 1
                    dfs(r, c)
                    
        return island_count
"""
    },
    "31_longest_consecutive_sequence.py": {
        "title": "Longest Consecutive Sequence (最长连续序列)",
        "difficulty": "Medium",
        "key_points": "哈希集合 (Hash Set) - O(N) 突破排序限制",
        "analysis_intuition": "直觉：最简单的方法是将数组排序，然后线性扫描寻找最长连续段，但这需要 O(N log N) 的时间复杂度。题目要求我们设计一个时间复杂度为 O(N) 的算法。",
        "analysis_derivation": "为了在不排序的前提下，在 O(N) 时间内找出最长连续段，我们可以利用哈希集合（查询复杂度为 O(1)）：\n1. 将所有数字存入哈希集合 `num_set`。\n2. 遍历集合中的每一个数 `num`：\n   - **破局点**：如何避免对同一个序列中的每个数字重复计数？我们只需要在遇到**序列的起点**时才开始向后累加。如何判断 `num` 是不是起点？如果 `num - 1` 不在集合中，说明没有比它小 1 的数，那么它就是这个连续序列的起点。\n   - 找到起点后，我们用一个循环不断判断 `num + 1`，`num + 2`... 是否在集合中，从而统计出该序列的长度。\n虽然内部有一个 `while` 循环，但由于我们限定了只有“起点”才会触发 `while` 循环，所以每个数字最多只会被访问两次（一次在外部遍历中，一次在 `while` 累加中）。因此，总时间复杂度依然是严格的 O(N)。",
        "code": """from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        \"\"\"
        时间复杂度: O(N) - 每个数字最多被处理常数次
        空间复杂度: O(N) - 存储哈希集合
        \"\"\"
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # 只有当 num - 1 不在集合中时，num 才是某段连续序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # 沿起点向后累加
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
"""
    },
    "32_alien_dictionary.py": {
        "title": "Alien Dictionary (外星人词典)",
        "difficulty": "Hard",
        "key_points": "拓扑排序 (Topological Sort) / 环路检测 / 字符串对齐比较",
        "analysis_intuition": "直觉：词典中单词是有序的，我们需要提取出字符之间的优先顺序。例如在英语字典中，'apple' 在 'banana' 之前是因为 'a' 的优先级高于 'b'。因此我们可以通过对比相邻两个单词的字符来构建字符间的有向边，然后跑拓扑排序。",
        "analysis_derivation": "1. **构建图**：相邻单词 `w1` 和 `w2` 对齐比较，找到第一个不同的字符 `c1` 和 `c2`。说明有一条有向边 `c1 -> c2`。如果出现 `w1` 是 `w2` 的前缀但 `len(w1) > len(w2)`（如 'abc' 在 'ab' 之前），这是非法的，直接返回空字符串。\n2. **拓扑排序 (DFS 三色标记法/BFS)**：我们用 DFS 检测环路。在 DFS 中，对每个节点使用三种状态标记：0 代表未访问，1 代表正在访问（递归栈中），2 代表已访问。若在搜索中遇到了状态 1 的节点，说明存在环，返回无效。若无环，DFS 退出时将节点压入结果栈，最后逆序输出即为拓扑排序结果。",
        "code": """from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        \"\"\"
        时间复杂度: O(C) - C 为所有单词中字符的总长度，建图和拓扑排序的复杂度均与字符总数呈线性关系
        空间复杂度: O(V + E) - V 为字符种类数（最大为 26），有向图邻接表空间
        \"\"\"
        # 初始化图的邻接表
        adj = {char: set() for word in words for char in word}
        
        # 1. 比较相邻单词，构建有向图
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # 边界异常检查：如果 w1 长于 w2 且 w2 是 w1 的前缀，说明非法（如 'abc' 排在 'ab' 前面）
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        # 2. DFS 环路检测与拓扑排序
        # visiting 记录正在递归访问的节点（检测环），visited 记录已处理完毕的节点
        visiting = set()
        visited = set()
        res = []
        
        def dfs(char):
            if char in visiting:
                return False  # 发现环路
            if char in visited:
                return True
                
            visiting.add(char)
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
            
        # 遍历图的所有节点跑 DFS
        for char in adj:
            if not dfs(char):
                return ""
                
        # 因为 DFS 在退出时才将节点入栈，所以拓扑排序结果需要反转
        return "".join(res[::-1])
"""
    },
    "33_graph_valid_tree.py": {
        "title": "Graph Valid Tree (以图判树)",
        "difficulty": "Medium",
        "key_points": "无向图环路检测 / 连通性校验 / 并查集 (Union Find)",
        "analysis_intuition": "直觉：一棵树本质上是一个**无环且连通**的无向图。在图论中，一个含有 `n` 个节点的图如果是一棵树，它必须满足两个核心条件：1. 边数刚好是 `n - 1`。 2. 图中没有任何环路（或者所有节点都是连通的）。",
        "analysis_derivation": "使用并查集 (Union Find) 来高效判断：\n1. 如果边的数量 `len(edges) != n - 1`，则直接判定不可能是树，返回 `False`。\n2. 初始化并查集。遍历所有的边 `(u, v)`，尝试在并查集中将 `u` 和 `v` 的集合合并：\n   - 如果合并前发现 `find(u) == find(v)`，说明 `u` 和 `v` 已经在同一个连通块中了，此时再加上这条边必然会在无向图中形成环。因此直接判定不是树，返回 `False`。\n   - 否则，合并两个连通块。\n3. 因为我们已经做过了边数 `len(edges) == n - 1` 的前置检查，且确认没有环，所以该图必然也是完全连通的。返回 `True` 即可。并查集的平均操作复杂度接近 O(1)。",
        "code": """from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        \"\"\"
        时间复杂度: O(N * alpha(N)) - alpha 是阿克曼函数的反函数，可视为常数 O(1)
        空间复杂度: O(N) - 并查集的 parent 数组
        \"\"\"
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
"""
    },
    "34_number_of_connected_components_in_an_undirected_graph.py": {
        "title": "Number of Connected Components in an Undirected Graph (无向图中连通分量的数目)",
        "difficulty": "Medium",
        "key_points": "无向图遍历 / 并查集 (Union Find)",
        "analysis_intuition": "直觉：给定一个无向图和它的所有边，我们需要找出有多少个互不连通的子图。我们可以用 DFS/BFS 遍历整个图，每开始一次遍历就代表找到了一个连通分量。但最简练的做法是使用并查集。",
        "analysis_derivation": "1. 初始状态下，我们假设图中有 `n` 个独立的节点，即连通分量初始数量为 `count = n`。\n2. 遍历所有的边 `(u, v)`：\n   - 通过并查集的 `find` 操作找到 `u` 和 `v` 的根节点。\n   - 如果它们的根节点不同，说明这两个原本独立的连通块之间有一条边相连。我们使用 `union` 操作将这两个连通块合并为一体，同时连通分量数 `count` 减 1。\n   - 如果根节点相同，说明它们原本就已经连通，不需要做任何改动。\n3. 遍历完所有的边之后，最后的 `count` 值即为无向图中连通分量的总数。",
        "code": """from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        \"\"\"
        时间复杂度: O(N + E * alpha(N)) - N 为节点数，E 为边数，均摊复杂度接近 O(N + E)
        空间复杂度: O(N) - 并查集 parent 数组
        \"\"\"
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
"""
    }
}
