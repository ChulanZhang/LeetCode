class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        m, k, n = len(mat1), len(mat2), len(mat2[0])
        mat1_valid = [[] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    mat1_valid[i].append((j, mat1[i][j]))

        mat2_valid = [[] for _ in range(k)]
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    mat2_valid[i].append((j, mat2[i][j]))
        
        results = [[0] * n for _ in range(m)]
        for i in range(m):
            for mat1_col, x in mat1_valid[i]:
                for j, y in mat2_valid[mat1_col]:
                    results[i][j] += x * y
        return results
# # 1 2 3
# # 4 5 6
# # 7 8 9

# # 1 1 1
# # 2 2 2
# # 3 3 3

# # [1, 2, 3] dot-product [1, 2, 3] = 1 + 4 + 9 = 14

# # results
# # 14 x x
# # x  x x
# # x  x x