class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # rotated = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n-1-i] = matrix[i][j]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = rotated[i][j]


        # optimal
        # step 1 transpose
        for i in range(n-1):
            for j in range(i,n):
                if i != j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # step 2 reverse the rows of matrix (transposed)
        for i in range(n):
            matrix[i].reverse()


        