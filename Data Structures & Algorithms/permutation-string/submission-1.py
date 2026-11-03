class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        if r > len(s2) : return False
        sol = [0]*26
        win = [0]*26
        for x in s1:
            sol[ord(x)-ord('a')] += 1
        for i in range(0,r):
            win[ord(s2[i])-ord('a')] += 1
        
        while l + r < len(s2):
            if sol == win : return True
            else:
                win[ord(s2[l])-ord('a')] -= 1
                l +=1
                win[ord(s2[l+r-1])-ord('a')] += 1
        if sol == win : return True
        return False
