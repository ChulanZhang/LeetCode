class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotation = transpose + flip column
        n = len(matrix)
        
        # transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # flip left/right
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

# dry run
# 1 2 3
# 4 5 6
# 7 8 9
# after transpose
# 1 4 7
# 2 5 8
# 3 6 9
# then flip
# 7 4 1
# 8 5 2
# 9 6 3

# what if it is counter clockwise rotate
# counter clockwise rotate = transpose + flip row

# time complexity: O(N^2)
# space complexity: O(1) inplace rotate