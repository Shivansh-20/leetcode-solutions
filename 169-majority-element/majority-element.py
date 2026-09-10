class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
            n = len(nums)
            if seen[i] > (n/2):
                return i