from typing import List, Optional, Dict, Set

# LeetCode 207: Course Schedule - Medium
# 🔗 Link: https://leetcode.com/problems/course-schedule/
# 🔑 Key Points: Topological Sort - Kahn's Algorithm (BFS) / DFS Cycle Detection
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The course prerequisite dependencies can be modeled as a directed graph where an edge from `A` to `B` means course `A` is a prerequisite for course `B`. To finish all courses, this directed graph must be a Directed Acyclic Graph (DAG) containing no cycles.
#   - Mathematical Derivation: 
#     A standard way to detect cycles in a directed graph is Topological Sort. We use Kahn's Algorithm (BFS-based):
#     1. Build an adjacency list and compute the in-degrees (number of incoming edges) for all nodes.
#     2. Add all nodes with an in-degree of 0 (courses with no prerequisites) to a queue.
#     3. While the queue is not empty, dequeue a node, increment the count of visited courses, and iterate through its neighbors. For each neighbor, decrement its in-degree by 1. If its in-degree drops to 0, enqueue it.
#     4. Finally, check if the visited count equals the total number of courses `numCourses`. If it does, a valid topological sort exists (no cycles); otherwise, there is a cycle.

from typing import List
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

