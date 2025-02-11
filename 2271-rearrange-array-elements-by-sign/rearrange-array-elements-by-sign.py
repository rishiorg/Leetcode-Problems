class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # new = []
        n = len(nums)
        # for i in range(n):
        #     if nums[i]>=0 and i%2==0:
        #         new.append(nums[i])
        #     elif nums[i]<0:
        #         new.append(nums[i])
        # return new
        pos = []
        neg=[]
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        result = []
        i, j = 0, 0
        while i < len(pos) and j < len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i += 1
            j += 1

        # Append remaining elements (if any)
        result.extend(pos[i:])
        result.extend(neg[j:])
        return result





        