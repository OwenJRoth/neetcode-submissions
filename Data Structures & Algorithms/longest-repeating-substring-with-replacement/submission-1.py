class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        winsize = 1
        rtn = 1
        storage = [0]*26
        storage[ord(s[0])-ord('A')] = 1
        while l+winsize < len(s):
            storage[ord(s[l+winsize])-ord('A')]+=1
            if winsize < max(storage) +k:
                winsize += 1
                rtn+=1
            else:
                storage[ord(s[l])-ord('A')]-=1
                l += 1
        return rtn