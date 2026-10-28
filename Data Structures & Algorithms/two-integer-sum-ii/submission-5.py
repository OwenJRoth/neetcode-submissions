class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0,len(numbers)):
            dic[target-numbers[i]] = i
        for x in range(0,len(numbers)):
            if dic.get(numbers[x]) is not None: return [x+1,1+dic[numbers[x]]]
        