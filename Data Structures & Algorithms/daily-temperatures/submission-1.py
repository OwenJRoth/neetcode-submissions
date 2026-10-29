class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        rtn=[0]*len(temperatures)
        for x in range(len(temperatures)-1,-1,-1):
            while  len(stack)>=1 and temperatures[x] >= temperatures[stack[-1]] :
                stack.pop()
            if len(stack) != 0:
                rtn[x] = stack[-1]-x
            stack.append(x)
        return rtn