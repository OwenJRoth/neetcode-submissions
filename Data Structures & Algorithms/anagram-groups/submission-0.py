class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn = [[]]
        counter =0
        dict = {}
        for s in strs:
            s2 = ''.join(sorted(s))
            if dict.get(s2) is None:
                dict[s2] = counter
                if counter != 0 : rtn.append([])
                rtn[counter].append(s)
                counter+=1
            else:
                rtn[dict.get(s2)].append(s)
        return rtn
        