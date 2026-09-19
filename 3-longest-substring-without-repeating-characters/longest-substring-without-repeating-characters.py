class Solution:
        def lengthOfLongestSubstring(self, s):
            l,r,chars = 0,0,{}
            max_l = 0
            n = len(s)
            while r < n:
                if s[r] in chars and l <= chars[s[r]] :
                    l = chars[s[r]] + 1
                chars[s[r]] = r
                length = r - l + 1
                max_l = max(max_l, length)
                r += 1
            return max_l


            
    
