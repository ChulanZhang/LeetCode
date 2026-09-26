class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rotten = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_r, new_c = r + dr, c + dc

                    if (
                        0 <= new_r < m and
                        0 <= new_c < n and
                        grid[new_r][new_c] == 1
                    ):
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        rotten.append((new_r, new_c))

            minutes += 1

        if fresh > 0:
            return -1
        else:
            return minutes