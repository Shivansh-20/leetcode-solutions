class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(start,end):
            dp = [0] * len(nums)
            dp[start] = nums[start]
            dp[start+1] = max(nums[start], nums[start+1])

            for i in range(start+2,end+1): #+1?
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[end] #??
        case_a = helper(0,n-2)
        case_b = helper(1,n-1)
        return max(case_a, case_b)
        


        
        