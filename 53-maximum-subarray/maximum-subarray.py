import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = -sys.maxsize - 1  # maximum sum
        n = len(nums)
        # for i in range(n):
        #     for j in range(i, n):
        #         # subarray = arr[i.....j]
        #         summ = 0

        #         # add all the elements of subarray:
        #         for k in range(i, j+1):
        #             summ += nums[k]

        #         maxi = max(maxi, summ)

        # return maxi


        # for i in range(n):
        #     sum = 0
        #     for j in range(i, n):
        #         # current subarray = arr[i.....j]

        #         #add the current element arr[j]
        #         # to the sum i.e. sum of arr[i...j-1]
        #         sum += nums[j]

        #         maxi = max(maxi, sum) # getting the maximum

        # return maxi
        sum = 0
        for i in range(n):
            sum+=nums[i]
            if sum >maxi:
                maxi=sum
            if sum<0:
                sum=0
            # if maxi<0:
            #     maxi=max(nums)
        return maxi


        