class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {0: 1, 1: 1}
        def helper(i):
            if i in dict:
                return dict[i]
            dict[i] = helper(i - 2) + helper(i - 1) #() because we are calling func not accesing by []
            return dict[i]
        return helper(n)