class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0 
        for i in range(1, n):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
        return left + 1

