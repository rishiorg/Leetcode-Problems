class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:  # Peak is on the right
                left = mid + 1
            else:  # Peak is on the left
                right = mid
        
        return left  # Peak index

        