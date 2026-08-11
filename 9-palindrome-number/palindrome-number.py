class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        digits = 0
        while x:
            digit = x % 10
            digits = digits * 10 + digit
            x //= 10
        return digits == temp
        
        