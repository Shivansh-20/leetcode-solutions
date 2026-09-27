class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if self.checker(s,left+1,right):
                    return True
                if self.checker(s,left,right-1):
                    return True
                return False
            left += 1
            right -= 1
        return True

        '''left += 1 #check by deleting left first
        if checker(s,left,right) == False: #call chcker on modified left
            right -= 1  #if false , modify right 
        checker(s,) # call checker again
        #if true return otherwise false '''

#handle length s < 2 seprately


    def checker(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1
        return True
            
        

        