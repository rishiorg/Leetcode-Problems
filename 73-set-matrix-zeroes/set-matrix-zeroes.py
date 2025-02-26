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
        row = [0]*n
        col = [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0


                    