class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #need dict to acess index 
        for i, x  in enumerate(nums):
            f = target - x
            if f in seen:
                return [seen[f],i] 
            seen[x] = i  #working with values so x is key and i is value

        