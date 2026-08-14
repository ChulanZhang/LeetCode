class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Use the first row and first col to record
        m, n = len(matrix), len(matrix[0])

        # Need to check if the first row and first col contains 0
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

# TC: O(m*n)
# SC: O(1)

#         m, n = len(matrix), len(matrix[0])
#         rows, cols = set(), set()
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)
        
#         for i in range(m):
#             for j in range(n):
#                 if i in rows or j in cols:
#                     matrix[i][j] = 0

# # TC: O(m*n)
# # CS: O(m+n)