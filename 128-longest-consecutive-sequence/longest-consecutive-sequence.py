class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #     longest = 1
    #     for i in range(len(nums)):
    #         x = nums[i]
    #         count = 1
    #         while (self.linearsearch(x+1,nums)==True):
    #             x=x+1
    #             count+=1
    #         longest = max(longest, count)
    #     return longest
        
    # def linearsearch(self,x,nums):
    #     for i in range(len(nums)):
    #         if nums[i]==x:
    #             return True
    #     return False




    # aprroach 2
        nums.sort()
        n = len(nums)
        if  n == 0:
            return 0
        longest = 1
        count = 0
        last_smaller = float('-inf')

        for i in range(n):
            if nums[i]-1 == last_smaller:
                count+=1
                last_smaller = nums[i]
            elif nums[i] == last_smaller:
                continue
            elif nums[i] != last_smaller:
                count = 1
                last_smaller = nums[i]
            longest = max(longest, count)
        return longest

        