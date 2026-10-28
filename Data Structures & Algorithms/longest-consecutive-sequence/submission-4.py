class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0 
        longest = 0

        for x in nums:
            length = 1
            longest = max(length,longest)
            if (x-1) not in numSet:
                while (x+length) in numSet:
                    length+=1
                    longest = max(length,longest)
            

        return longest
            
