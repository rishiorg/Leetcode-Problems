class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = max(nums)
        mini = min(nums)
        if n<3:
            return -1
        nums.remove(maxi)
        nums.remove(mini)
        # for i in nums:
        #     if i != maxi and nums != mini:
        #         return i
        return nums[0]