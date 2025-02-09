class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {}  # Dictionary to store (value -> index)

        for i, num in enumerate(nums):
            complement = target - num  # Find the required pair value

            if complement in index_map:
                return [index_map[complement], i]  # Return indices of both numbers
        
            index_map[num] = i  # Store the index of current number

        return []

        