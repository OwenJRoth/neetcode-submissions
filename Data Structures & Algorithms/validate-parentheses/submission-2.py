class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if dic.get(i) is None: stack.append(i)
            elif len(stack) == 0 :return False
            elif stack.pop() != dic[i]: return False
        if len(stack) != 0: return False
        return True
