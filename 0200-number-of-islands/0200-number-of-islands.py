class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        results = 0

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            grid[x][y] = "0"

            while len(queue) > 0:
                x, y = queue.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0<= new_y < m and grid[new_x][new_y] == "1":
                        grid[new_x][new_y] = "0"
                        queue.append((new_x, new_y))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    results += 1
                    print(results)
                    bfs(i, j)
        return results


        