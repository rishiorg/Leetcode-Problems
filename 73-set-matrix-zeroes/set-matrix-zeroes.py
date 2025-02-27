class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
    #     count = 0
    #     for i in range(n):
    #         for j in range(m):
    #             if matrix[i][j]==0:
    #                 count+=1
    #     if count == 0:
    #         return matrix
    #     for i in range(n):
    #         for j in range(m):
    #             if matrix[i][j]==0:
    #                 self.setrow(matrix,n,m,i)
    #                 self.setcol(matrix,n,m,j)
    #     for i in range(n):
    #         for j in range(m):
    #             if matrix[i][j]==-1:
    #                 matrix[i][j]=0
    # def setrow(self,matrix,n,m,i):
    #     for j in range(m):
    #         if matrix[i][j] != 0:
    #             matrix[i][j] = -1
    # def setcol(self,matrix,n,m,j):
    #     for i in range(n):
    #         if matrix[i][j] != 0:
    #             matrix[i][j]=-1
        # row = [0]*n
        # col = [0]*m
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             row[i] = 1
        #             col[j] = 1
        
        # for i in range(n):
        #     for j in range(m):
        #         if row[i] or col[j]:
        #             matrix[i][j] = 0

        # new row matrix[..][0]
        # new col matrix[0][..]
        col0 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark ith row
                    matrix[i][0] = 0
                    # mark jth col
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0


                    