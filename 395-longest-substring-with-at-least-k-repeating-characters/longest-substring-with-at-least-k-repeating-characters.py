class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if freq[char] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1:], k)
                return max(left, right)

        return len(s)

            