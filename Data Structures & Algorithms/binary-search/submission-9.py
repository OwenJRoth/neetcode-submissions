class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        temp = None 
        if end == 0 and nums[0]==target: return 0
        while True:
            temp = int((start+end)/2)
            if nums[temp] == target:
                return temp
            if len(nums[start:end]) <= 2:
                if nums[start] == target : return start
                elif nums[end] == target : return end
                else: break
            if nums[temp] < target:
                start = temp
            else: end = temp
            
        return -1

