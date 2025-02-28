class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ls = []
        n = len(nums)
        # for i in range(n):
        #     if len(ls) == 0 or ls[0] != nums[i]:
        #         cnt = 0
        #         for j in range(n):
        #             if nums[i]==nums[j]:
        #                 cnt+=1
        #         if cnt > n//3:
        #             ls.append(nums[i])
        #     if len(ls) == 2:
        #         break
        # return ls
         
        #  hashmap approach
        hashmap = defaultdict(int) 
        ls = []
        mini = n//3 +1
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] >= mini and num not in ls:
                ls.append(num)
        return ls

        