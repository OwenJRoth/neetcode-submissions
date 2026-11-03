class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin = prices[0]
        rtn = 0
        for x in prices:
            lmin = min(lmin,x)
            rtn = max(rtn, x-lmin)
        return rtn
