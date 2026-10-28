class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tdict = {}
        sdict = {}
        for i in t:
            if tdict.get(i) is None: tdict[i] = 1
            else : tdict[i] += 1
        for j in s:
            if sdict.get(j) is None: sdict[j] = 1
            else : sdict[j] += 1
        for k in tdict:
            if sdict.get(k) is None : return False
            if sdict[k] != tdict[k] : return False
        for l in sdict:
            if tdict.get(l) is None : return False
            if tdict[l] != sdict[l] : return False

        return True