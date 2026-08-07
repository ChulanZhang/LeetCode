# Graph category data
PROBLEMS = {
    "27_clone_graph.py": {
        "title": "Clone Graph",
        "difficulty": "Medium",
        "key_points": "Graph Traversals - DFS / BFS with Hash Map Mapping",
        "analysis_intuition": "To clone a graph, we must traverse all of its nodes. However, because graphs can contain cycles, we must keep track of nodes we have already copied to prevent falling into infinite recursion.",
        "analysis_derivation": "We use a hash map `cloned` to store the mapping from original nodes to their cloned counterparts (`old_node -> new_node`).\nFor each visited node:\n1. If it is already in `cloned`, return the cloned node directly.\n2. Otherwise, instantiate a new node with the same value and save it in `cloned`.\n3. Recursively copy all its neighbors, adding each cloned neighbor to the new node's neighbor list.\nThis DFS + Hash Map pattern ensures every node and edge is copied once without cycles.",
        "code": """class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Time Complexity: O(V + E) - Each node and edge is visited once
        # Space Complexity: O(V) - Recursion stack and cloned hash map
        if not node:
            return None
            
        cloned = {}
        
        def dfs(curr):
            # If already cloned, return the cached clone to break cycles
            if curr in cloned:
                return cloned[curr]
                
            # Instantiate the copy and cache it immediately
            copy = Node(curr.val)
            cloned[curr] = copy
            
            # Recursively copy all neighbor nodes
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)
"""
    },
    "28_course_schedule.py": {
        "title": "Course Schedule",
        "difficulty": "Medium",
        "key_points": "Topological Sort - Kahn's Algorithm (BFS) / DFS Cycle Detection",
        "analysis_intuition": "The course prerequisite dependencies can be modeled as a directed graph where an edge from `A` to `B` means course `A` is a prerequisite for course `B`. To finish all courses, this directed graph must be a Directed Acyclic Graph (DAG) containing no cycles.",
        "analysis_derivation": "A standard way to detect cycles in a directed graph is Topological Sort. We use Kahn's Algorithm (BFS-based):\n1. Build an adjacency list and compute the in-degrees (number of incoming edges) for all nodes.\n2. Add all nodes with an in-degree of 0 (courses with no prerequisites) to a queue.\n3. While the queue is not empty, dequeue a node, increment the count of visited courses, and iterate through its neighbors. For each neighbor, decrement its in-degree by 1. If its in-degree drops to 0, enqueue it.\n4. Finally, check if the visited count equals the total number of courses `numCourses`. If it does, a valid topological sort exists (no cycles); otherwise, there is a cycle.",
        "code": """from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time Complexity: O(V + E) - V is the number of courses, E is the number of prerequisites
        # Space Complexity: O(V + E) - Adjacency list and in-degree table
        
        # Build adjacency list and in-degree array
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
            
        # Dequeue starting courses with 0 prerequisites (in-degree = 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited_count = 0
        
        while queue:
            curr = queue.popleft()
            visited_count += 1
            
            # Decrement in-degree for all depending neighbors
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                # Enqueue neighbor if all its prerequisites are completed
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return visited_count == numCourses
"""
    },
    "29_pacific_atlantic_water_flow.py": {
        "title": "Pacific Atlantic Water Flow",
        "difficulty": "Medium",
        "key_points": "Multi-Source DFS / Reverse Search",
        "analysis_intuition": "We need to find grid coordinates that can flow to both the Pacific Ocean (top/left) and the Atlantic Ocean (bottom/right). Running a separate flow search from every cell would take O((M * N)^2) time, which is too slow.",
        "analysis_derivation": "Reverse thinking: Instead of starting from each grid cell and searching downwards to the oceans, we start from the ocean boundaries and search backwards (climbing up to adjacent cells with height >= current height).\n1. Declare two boolean matrices: `pacific_reach` and `atlantic_reach` to store reachable coordinates from the respective ocean.\n2. Run DFS from the Pacific boundaries (first row and first column) to mark all reachable cells.\n3. Run DFS from the Atlantic boundaries (last row and last column) to mark all reachable cells.\n4. Traverse the grid. Any cell marked True in both matrices can flow to both oceans. This reduces the time complexity to O(M * N).",
        "code": """from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(m * n) - Each cell is visited a constant number of times
        # Space Complexity: O(m * n) - Reachability grids and recursive DFS stack
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_reach = [[False] * n for _ in range(m)]
        atlantic_reach = [[False] * n for _ in range(m)]
        
        def dfs(r, c, reach, prev_height):
            # Base cases: out of bounds, already visited, or water cannot flow backwards (height < prev_height)
            if (r < 0 or r >= m or c < 0 or c >= n or 
                reach[r][c] or heights[r][c] < prev_height):
                return
            reach[r][c] = True
            
            # Explore 4 directions
            dfs(r + 1, c, reach, heights[r][c])
            dfs(r - 1, c, reach, heights[r][c])
            dfs(r, c + 1, reach, heights[r][c])
            dfs(r, c - 1, reach, heights[r][c])
            
        # Run DFS from the Pacific and Atlantic boundaries
        for i in range(m):
            dfs(i, 0, pacific_reach, heights[i][0])
            dfs(i, n - 1, atlantic_reach, heights[i][n - 1])
        for j in range(n):
            dfs(0, j, pacific_reach, heights[0][j])
            dfs(m - 1, j, atlantic_reach, heights[m - 1][j])
            
        # Find intersections of Pacific and Atlantic reachability
        res = []
        for r in range(m):
            for c in range(n):
                if pacific_reach[r][c] and atlantic_reach[r][c]:
                    res.append([r, c])
        return res
"""
    },
    "30_number_of_islands.py": {
        "title": "Number of Islands",
        "difficulty": "Medium",
        "key_points": "Grid Search - DFS / BFS / Union-Find",
        "analysis_intuition": "We need to find the number of connected components of '1's (land) surrounded by '0's (water). When we encounter a '1', it marks the discovery of a new island. We must then run DFS/BFS to traverse and sink all connected lands to avoid double counting.",
        "analysis_derivation": "1. Iterate through every cell `(r, c)` of the grid.\n2. If `grid[r][c] == '1'`:\n   - Increment the island counter.\n   - Start DFS from `(r, c)`. For each adjacent land cell, we sink it by setting its value to `'0'` (in-place modification is a great space optimization that avoids a `visited` set).\n3. Continue scanning the grid; any future `'1'` encountered must belong to a separate, new island.",
        "code": """from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity: O(m * n) - Each grid cell is visited a constant number of times
        # Space Complexity: O(m * n) - Recursion stack in the worst case (all land)
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base cases: out of bounds or water cell
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            # Sink current land to prevent visiting it again
            grid[r][c] = '0'
            # Recursively explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    island_count += 1
                    # Initiate DFS to sink all connected parts of the island
                    dfs(r, c)
                    
        return island_count
"""
    },
    "31_longest_consecutive_sequence.py": {
        "title": "Longest Consecutive Sequence",
        "difficulty": "Medium",
        "key_points": "Hash Set - O(N) Time Optimization",
        "analysis_intuition": "Sorting the array and scanning takes O(N log N) time complexity. We need to find an O(N) solution using extra memory.",
        "analysis_derivation": "To achieve O(N) time complexity, we can use a hash set for O(1) membership lookups:\n1. Insert all numbers into a hash set `num_set`.\n2. Iterate through each number `num` in the set:\n   - Check if `num - 1` is in the set. If it is not, then `num` is the starting element of a consecutive sequence.\n   - From this starting element, increment and check for `num + 1`, `num + 2`... in the set, counting the length of this sequence.\n   - Update the global maximum length.\nSince a sequence is only checked from its absolute starting element, each number is processed at most twice, yielding a strictly linear O(N) time complexity.",
        "code": """from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time Complexity: O(N) - Each number is processed at most twice
        # Space Complexity: O(N) - Storage for the hash set
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Check for consecutive elements
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
"""
    },
    "32_alien_dictionary.py": {
        "title": "Alien Dictionary",
        "difficulty": "Hard",
        "key_points": "Topological Sort / Cycle Detection / Directed Graphs",
        "analysis_intuition": "Given a sorted list of words in an alien language, we need to extract the order of characters. In a dictionary, word ordering is determined by the first differing character. We can build directed edges `c1 -> c2` by comparing adjacent words and then run a topological sort.",
        "analysis_derivation": "1. **Graph Construction**: Compare adjacent words `w1` and `w2` character by character. The first mismatch `w1[j] != w2[j]` gives an edge `w1[j] -> w2[j]`. If `w1` is longer than `w2` and `w2` is a prefix of `w1` (e.g., 'abc' comes before 'ab'), this is an invalid order, so we return \"\".\n2. **Topological Sort (DFS / BFS)**: Run DFS with three-state coloring (0: unvisited, 1: visiting, 2: visited) to detect cycles. If we encounter a node in state 1 during DFS, there is a cycle, so we return \"\". If the graph is acyclic, reverse the DFS finish order to get the topological order.",
        "code": """from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Time Complexity: O(C) - C is the total length of all words combined
        # Space Complexity: O(V + E) - Adjacency list representation (V <= 26)
        
        # Initialize graph adjacency list
        adj = {char: set() for word in words for char in word}
        
        # 1. Build directed graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # Prefix boundary check: if w1 is longer and has w2 as prefix, order is invalid
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        # 2. Cycle detection and topological sort using DFS
        visiting = set()  # Set of nodes currently in recursion stack
        visited = set()   # Set of nodes fully processed
        res = []
        
        def dfs(char):
            if char in visiting:
                return False  # Cycle detected
            if char in visited:
                return True
                
            visiting.add(char)
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)  # Append node after exploring all paths from it
            return True
            
        for char in adj:
            if not dfs(char):
                return ""  # Cycle exists, return empty
                
        # Reverse the result list since DFS returns reverse order
        return "".join(res[::-1])
"""
    },
    "33_graph_valid_tree.py": {
        "title": "Graph Valid Tree",
        "difficulty": "Medium",
        "key_points": "Undirected Graph - Cycle Detection & Connectivity / Union-Find",
        "analysis_intuition": "An undirected graph is a tree if and only if it is **connected and acyclic**. In graph theory, a graph with `n` nodes is a tree if: 1. It has exactly `n - 1` edges. 2. It contains no cycles.",
        "analysis_derivation": "We can use Union-Find (Disjoint Set) to check this efficiently:\n1. If `len(edges) != n - 1`, the graph cannot be a tree, return False.\n2. Initialize a disjoint set. Iterate through each edge `(u, v)` and try to union their sets:\n   - If `find(u) == find(v)` before union, `u` and `v` are already connected, so adding this edge creates a cycle. Return False.\n   - Otherwise, union their sets.\n3. Since we have verified `edges == n - 1` and confirmed no cycles, the graph is guaranteed to be fully connected. Return True.",
        "code": """from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time Complexity: O(N * alpha(N)) - alpha is the inverse Ackermann function, roughly O(1)
        # Space Complexity: O(N) - Disjoint Set parent array
        
        # Necessary condition: tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        parent = [i for i in range(n)]
        
        def find(i):
            if parent[i] == i:
                return i
            # Path compression optimization
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            # If roots are same, a cycle is detected
            if root_i == root_j:
                return False
            parent[root_i] = root_j
            return True
            
        for u, v in edges:
            if not union(u, v):
                return False  # Cycle detected
                
        return True
"""
    },
    "34_number_of_connected_components_in_an_undirected_graph.py": {
        "title": "Number of Connected Components in an Undirected Graph",
        "difficulty": "Medium",
        "key_points": "Connected Components / Union-Find",
        "analysis_intuition": "Given an undirected graph, we need to find the number of disconnected subgraphs. While DFS/BFS traversal works, Union-Find provides a highly concise and efficient disjoint set union solution.",
        "analysis_derivation": "1. Initially, assume all `n` nodes are isolated components (`count = n`).\n2. Iterate through each edge `(u, v)`:\n   - Find the roots of `u` and `v` in the disjoint set.\n   - If the roots are different, they belong to different components. We merge (union) the sets and decrement `count` by 1.\n   - If they have the same root, they are already connected, so we do nothing.\n3. The final value of `count` is the number of connected components.",
        "code": """from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Time Complexity: O(N + E * alpha(N)) - N nodes, E edges. Virtually O(N + E)
        # Space Complexity: O(N) - Disjoint Set parent array
        parent = [i for i in range(n)]
        count = n
        
        def find(i):
            if parent[i] == i:
                return i
            # Path compression
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            nonlocal count
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Merge the components
                parent[root_i] = root_j
                # Decrement component count upon successful merge
                count -= 1
                
        for u, v in edges:
            union(u, v)
            
        return count
"""
    }
}
