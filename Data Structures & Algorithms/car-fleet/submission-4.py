class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posdict = {}
        temp=0
        for x,y in enumerate(position):
            temp = ((target-y)/speed[x])
            if posdict.get(y) == None:
                posdict[y] = temp
            else: posdict[y] = min(posdict[y], temp)
        rtn = []
        sortedset = sorted(set(position),reverse = True)
        for key in sortedset:
            if len(rtn) == 0: rtn.append(posdict[key])
            elif rtn[-1] < posdict[key]:rtn.append(posdict[key])
        return len(rtn)
