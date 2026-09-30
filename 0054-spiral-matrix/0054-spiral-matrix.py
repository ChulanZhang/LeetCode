class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left, top, right, down = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        results = []

        while left <= right and top <= down:
            for x in range(left, right + 1):
                results.append(matrix[top][x])
            top += 1
            for y in range(top, down + 1):
                results.append(matrix[y][right])
            right -= 1
            if top <= down:
                for x in range(right, left - 1, -1):
                    results.append(matrix[down][x])
                down -= 1
            if left <= right:
                for y in range(down, top - 1, -1):
                    results.append(matrix[y][left])
                left += 1
        return results

        