class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # diff = 0
        # maxdiff= 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff = prices[j]-prices[i]
        #         maxdiff=max(maxdiff,diff)
        # return maxdiff

        mini = float('inf')
        maxprofit = 0
        for i in prices:
            mini = min(mini,i)
            maxprofit = max(maxprofit,i-mini)
        return maxprofit


        