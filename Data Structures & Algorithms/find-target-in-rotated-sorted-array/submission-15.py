class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        mid = 0
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[lo] == target: return lo
            if nums[hi] == target: return hi
            if nums[mid] < target:
                if target < nums[hi] or nums[mid] > nums[hi]:
                    lo = mid + 1
                else: hi = mid
            elif nums[mid] > target:
                if target > nums[lo] or nums[lo] > nums[mid]:
                    hi = mid
                else: lo = mid + 1
            else : return mid
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        else: return -1