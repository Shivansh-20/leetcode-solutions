class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        start = 0
        current_sum = 0
        max_l = 0
        for end, num in enumerate(nums):
            current_sum += num
            while num * (end-start + 1) - current_sum > k:
                current_sum -= nums[start]
                start += 1
            max_l = max(max_l, end-start +1)
        return max_l

        