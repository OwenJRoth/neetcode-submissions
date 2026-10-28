class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        nums.sort()
        store = [1]
        for x in range(1,len(nums)):
            if nums[x-1] == nums[x] : store.append(store[x-1])
            elif nums[x-1] == nums[x]-1: store.append(store[x-1]+1)
            else: store.append(1)
        print(store)
        return max(store)
            
