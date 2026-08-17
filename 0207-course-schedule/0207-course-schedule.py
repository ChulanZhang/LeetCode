class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph[i] represent the courses unlocked by course i
        graph = [[] for _ in range(numCourses)]
        # indegree[i] is the number of unfinished prerequisites
        indegree = [0] * numCourses

        # Build the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Create the queue with courses without requiring any prereq
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        visited = 0

        while queue:
            course = queue.popleft()
            visited += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return visited == numCourses


        