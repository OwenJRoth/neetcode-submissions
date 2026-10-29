class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1 : return 0
        l = 0
        r = len(height)-1
        maxl= height[l]
        maxr = height[r]
        temp = 0
        rtn = 0
        while l < r:
            if maxl > maxr:
                #
                r-=1
                maxr = max(maxr, height[r])
                temp = min(maxl,maxr) - height[r]
                if temp > 0 : rtn += temp
            else:
                l +=1
                maxl = max(maxl, height[l])
                temp = min(maxl,maxr) - height[l]
                if temp > 0 : rtn += temp
        return rtn