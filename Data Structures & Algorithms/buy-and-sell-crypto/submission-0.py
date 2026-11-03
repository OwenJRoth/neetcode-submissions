class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmax = 0
        rtn = 0
        for x in range(len(prices)-1,-1,-1):
            lmax = max(lmax,prices[x])
            rtn = max(rtn, lmax-prices[x])
        return rtn
