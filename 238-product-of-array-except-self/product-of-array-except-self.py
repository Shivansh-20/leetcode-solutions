class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        product = 1
        ans = [1] * n
        for i in range(n):
            #storing here,
            ans[i] *= product 
            product *= nums[i] 
        product = 1
        for i in range(n-1,-1,-1):
            ans[i] *= product
            product *= nums[i]
        return ans 

        