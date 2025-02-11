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
        # pos = []
        # neg=[]
        # for i in nums:
        #     if i >= 0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
        # result = []
        # i, j = 0, 0
        # while i < len(pos) and j < len(neg):
        #     result.append(pos[i])
        #     result.append(neg[j])
        #     i += 1
        #     j += 1

        # # Append remaining elements (if any)
        # result.extend(pos[i:])
        # result.extend(neg[j:])
        # return result
        n = len(nums)
    
    # Define array for storing the ans separately.
        ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
        posIndex, negIndex = 0, 1
        for i in range(n):
            
            # Fill negative elements in odd indices and inc by 2.
            if nums[i] < 0:
                ans[negIndex] = nums[i]
                negIndex += 2
            
            # Fill positive elements in even indices and inc by 2.
            else:
                ans[posIndex] = nums[i]
                posIndex += 2
        
        return ans
        





        