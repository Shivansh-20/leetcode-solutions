class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x  #x -1 only for x > 2
        while l <= h:
            mid = (l+h) // 2
            m = mid ** 2
            if m <= x:
                l  = mid + 1
            elif m > x:
                h = mid - 1
        return l - 1  

        