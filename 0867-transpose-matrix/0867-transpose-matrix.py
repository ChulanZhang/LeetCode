class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # matrix = [[1,2,3],[4,5,6]]
        # [1, 2, 3]
        # [4, 5, 6]

        # [1, 4]
        # [2, 5]
        # [3, 6]
        n, m = len(matrix), len(matrix[0])
        results = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                results[j][i] = matrix[i][j]
        
        return results

# 