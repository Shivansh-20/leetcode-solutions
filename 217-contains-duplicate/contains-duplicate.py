class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

       #seen = set()
        '''for i in nums:
            if i in seen:
                return True 
            seen.add(i)
        return False'''

        


        