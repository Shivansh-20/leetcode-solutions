class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left = 0
        right = len(nums) - 1
        mid = 0
        while mid <= right:
            if nums[mid] == 2:
                nums[mid],nums[right] = nums[right],nums[mid]
                right -= 1
                #cannot move mid need to examine new value at same index
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[left] = nums[left],nums[mid]
                left += 1
                mid += 1
        return nums
