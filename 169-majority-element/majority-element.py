from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count,count1=0,0
        # li = []
        # for i in nums:
        #     count1=0
        #     for j in nums:
        #         if i == j:
        #             count1+=1
        #     count = max(count,count1)
        #     if count>len(nums)//2:
        #         return i
        counts = Counter(nums)
        for key, value in counts.items():
            if value>(len(nums)//2):
                return key
        return -1