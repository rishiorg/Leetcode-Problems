class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)  # size of the given array.
        cnt = 0  # Number of subarrays.

        # for i in range(n):  # starting index i.
        #     suma = 0
        #     for j in range(i, n):  # ending index j.
        #         # calculate the sum of subarray [i...j].
        #         # subarray_sum = sum(nums[i:j+1])
        #         suma += nums[j]

        #         # Increase the count if sum == k.
        #         if suma == k:
        #             cnt += 1
        prefixSum = 0
        mpp = defaultdict(int)
        mpp[0]=1
        for i in range(n):
            prefixSum+=nums[i]
            remove = prefixSum - k
            cnt += mpp[remove]
            mpp[prefixSum]+=1
        return cnt
        