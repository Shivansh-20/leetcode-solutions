class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n > 1:
            seen.add(n)
            square_sum = 0
            n = self.helper(n,square_sum) #missing self you can't , fucntion calls itself
        return n == 1
    
    def helper(self,n,square_sum):
            while n:
                digit = n % 10
                square_sum += digit * digit
                n //= 10
            return square_sum
        