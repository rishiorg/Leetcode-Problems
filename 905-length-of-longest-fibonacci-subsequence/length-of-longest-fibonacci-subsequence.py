class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index = {x: i for i, x in enumerate(arr)}  # Store index of each value in arr
        dp = defaultdict(lambda: 2)  # Default length is 2 (minimum required)
        max_len = 0

        for i in range(len(arr)):
            for j in range(i):
                prev = arr[i] - arr[j]  # Find arr[k] such that arr[k] + arr[j] = arr[i]
                if prev in index and index[prev] < j:  # Ensure k < j < i
                    k = index[prev]
                    dp[(j, i)] = dp[(k, j)] + 1
                    max_len = max(max_len, dp[(j, i)])

        return max_len if max_len >= 3 else 0  # If length < 3, return 0 (no valid sequence)
        