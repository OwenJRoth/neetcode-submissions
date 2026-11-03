class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        if len(s) == 0 : return 0
        rtn = 1
        pointer = 0
        for i in range(0,len(s)):
            if last.get(s[i]) is None:
                last[s[i]] = i
            else:
                if pointer <= last[s[i]] : pointer = last[s[i]]+1
                last[s[i]] = i
            rtn = max(rtn, (i+1-pointer))
        return rtn
