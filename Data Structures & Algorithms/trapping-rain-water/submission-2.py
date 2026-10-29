class Solution:
    def trap(self, height: List[int]) -> int:
        forward = [None]*len(height)
        backward = [None]*len(height)
        fmax, bmax = 0, 0
        rtn = 0
        for i in range(0,len(height)):
            fmax = max(fmax,height[i])
            bmax = max(bmax,height[-1-i])
            forward[i] = fmax
            backward[-1-i] = bmax
        for i in range(0, len(height)):
            rtn += min(forward[i],backward[i])-height[i]
        return rtn
