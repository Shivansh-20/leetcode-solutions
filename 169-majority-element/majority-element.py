class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1  #Give me the value associated with key i. If i doesn't exist, #give me 0 , add + 1 to it 
            n = len(nums)
            if seen[i] > (n/2):
                return i