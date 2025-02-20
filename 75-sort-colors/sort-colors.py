class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count1,count0,count2 = 0,0,0
        for i  in nums:
            if i == 0:
                count0+=1
            if i == 1:
                count1+=1
            if i == 2:
                count2+=1
        del nums[:]
        for i in range(count0):
            nums.append(0)
        for i in range(count1):
            nums.append(1)
        for i in range(count2):
            nums.append(2)
        # n=len(nums)
        # low = 0
        # mid = 0
        # high = n-1

        # while mid<=high:
        #     if nums[mid] == 0:
        #         nums[mid],nums[low]=nums[low],nums[mid]
        #         low+=1
        #         mid+=1
        #     elif nums[mid]==1:
        #         mid+=1
        #     elif nums[mid]==2:
        #         nums[mid],nums[high]=nums[high],nums[mid]
        #         high-=1

        