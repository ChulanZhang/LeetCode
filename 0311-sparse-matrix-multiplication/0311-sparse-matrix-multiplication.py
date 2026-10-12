class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
#         # results[i][j] = mat1's ith row * mat2's jth col 
#         # mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
#         # [1,0,0] dot_product [7,0,0] = 7 at results[0][0]
#         # results[i][j] = sum of 
        results = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row_idx, row in enumerate(mat1):
            for element_idx, row_element in enumerate(row):
                # mat1[i][k]
                if row_element:
                    #mat2[k][:]
                    for col_idx, col_element in enumerate(mat2[element_idx]):
                        # results[i][:]
                        results[row_idx][col_idx] += row_element * col_element
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


        # m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        # g1 = [[] for _ in range(m)]
        # for i in range(m):
        #     for col in range(k):
        #         if mat1[i][col] != 0:
        #             g1[i].append((col, mat1[i][col]))
        
        # g2 = [[] for _ in range(k)]
        # for row in range(k):
        #     for j in range(n):
        #         if mat2[row][j] != 0:
        #             g2[row].append((j, mat2[row][j]))
        
        # results = [[0] * n for _ in range(m)]

        # for i in range(m):
        #     for col_k, x in g1[i]:
        #         for j, y in g2[col_k]:
        #             results[i][j] += x * y
        
        # return results