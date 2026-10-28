class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        rtn = []
        temp = 1
        for n in nums[0:-1] :
            temp *= n
            pre.append(temp)
        temp=1
        for s in range(len(nums)-1,0,-1):
            temp *= nums[s]
            post.append(temp)
        #print(pre)
        #print(post)
        for i in range(0,len(nums)):
            if i == len(nums)-1:
                rtn.append(pre[i-1])
            elif i == 0:
                rtn.append(post[-1])
            else   : 
                rtn.append(pre[i-1]*post[-i-1])
        return rtn