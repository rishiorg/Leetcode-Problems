class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if we need to return the specific element 
        def nCr(n,r):
            res = 1

            # calculating nCr:
            for i in range(r):
                res = res * (n - i)
                res = res // (i + 1)
            return res

        #     return res
        # element = nCr(r - 1, c - 1)
        # return element

        # specific row
        # ans = 1
        # print(ans, end=" ") # printing 1st element

        # #Printing the rest of the part:
        # for i in range(1, n):
        #     ans = ans * (n - i)
        #     ans = ans // i
        #     print(ans, end=" ")
        # print()

        #brute
        ans = []
        for i in range(numRows):
            tempList = []
            for j in range(i+1):
                tempList.append(nCr(i,j))
            ans.append(tempList)
        return  ans
