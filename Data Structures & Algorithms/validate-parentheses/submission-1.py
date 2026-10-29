class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 : return True
        dic = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if dic.get(i) is None: stack.append(i)
            elif len(stack) == 0 :return False
            elif stack.pop() != dic[i]: return False
        if len(stack) != 0: return False
        return True
