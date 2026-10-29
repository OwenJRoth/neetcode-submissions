class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rtn = []
        for i in range(0,len(nums)):
            if nums[i] == nums[i-1] and i !=0: continue
            l,r = i+1,len(nums)-1
            while l < r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0 : 
                    rtn.append([nums[i],nums[l],nums[r]])
                    while l< r and nums[r] == nums[r-1]: r-=1
                    r-=1
                elif sum <0:
                    while l<r and nums[l] == nums[l+1]: l+=1
                    l+=1
                elif sum>0:
                    while l< r and nums[r] == nums[r-1]: r-=1
                    r-=1
                
        return rtn


        