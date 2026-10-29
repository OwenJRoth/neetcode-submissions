class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        for x in tokens:
            try:
                numstack.append(int(x))
            except:
                b = numstack.pop()
                a = numstack.pop()
                match x:
                    case '*':
                        numstack.append(a*b)
                    case '/':
                        numstack.append(int(a/b))
                    case '+':
                        numstack.append(a+b)
                    case '-':
                        numstack.append(a-b)
            
        return numstack.pop()
                