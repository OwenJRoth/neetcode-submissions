import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        for x in range(0,len(s)):
            print([s[x].upper(),s[-x-1].upper(),])
            if s[x].upper()!=s[-x-1].upper() : return False
        return True