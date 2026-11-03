class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        if len(s) == 0 : return 0
        rtn = 0
        pointer = 0
        for i in range(0,len(s)):
            if s[i] in last:
                pointer = max(last[s[i]]+1,pointer)
            last[s[i]] = i
            rtn = max(rtn, (i-pointer+1))
        return rtn
