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
        # hashmap = defaultdict(int) 
        # ls = []
        # mini = n//3 +1
        # for num in nums:
        #     hashmap[num] += 1
        #     if hashmap[num] >= mini and num not in ls:
        #         ls.append(num)
        # return ls

        # optimal
        count1,count2 = 0,0
        ele1,ele2 = float('-inf'), float('-inf')
        for i in range(n):
            if count1 == 0 and nums[i] != ele2:
                count1 = 1
                ele1 = nums[i]
            elif count2 == 0 and nums[i] != ele1:
                count2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                count1+=1
            elif nums[i] == ele2:
                count2+=1
            else:
                count1-=1
                count2-=1
        ls = []
        count1,count2 = 0,0
        mini = n//3 +1
        for i in nums:
            if ele1 == i:
                count1+=1
            elif ele2 == i:
                count2+=1
        if count1 >= mini:
            ls.append(ele1)
        if count2 >= mini:
            ls.append(ele2)
        # ls.sort()
        return ls

        