class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0,len(nums)):
            if dic.get(nums[i]) is None :
                dic[target-nums[i]] = i
        for i in range(0,len(nums)):
            if dic.get(nums[i]) is not None and dic.get(nums[i]) != i:
                return [dic.get(nums[i]), i]