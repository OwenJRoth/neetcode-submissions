class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        temp = 0
        for x,y in enumerate(heights):
            temp = [0,0]
            if len(stack) == 0 and y > 0:
                stack.append([x,y])
            elif len(stack) != 0 and stack[-1][-1] > y:
                while len(stack) > 0 and stack[-1][-1] > y:
                    temp = stack.pop()
                    res = max(res, temp[-1]*(x-temp[0]))
            if len(stack) == 0 or stack[-1][-1] < y:
                if temp == [0,0]:
                    stack.append([x,y])
                else: stack.append([temp[0],y])
        while len(stack) != 0:
            temp = stack.pop()
            res = max(res, temp[-1]*((len(heights))-temp[0]))
        return res
