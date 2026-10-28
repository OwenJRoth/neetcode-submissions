
class Solution:
    def encode(self, strs: List[str]) -> str:
        self.dummy = []
        rtn = ''
        for s in strs:
            rtn+= s
            self.dummy.append(len(s))
        return rtn

    def decode(self, s: str) -> List[str]:
        rtn=[]
        #if s == '' : return [""]
        prev = 0
        for c in self.dummy:
            c+=prev
            rtn.append(s[prev:c])
            prev = c
        return rtn
