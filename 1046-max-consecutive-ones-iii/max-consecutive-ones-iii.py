class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start, end, current_zero = 0,0,0
        size_w, max_w = 0,0
        n = len(nums)
        for end in range(n):
            if nums[end] == 0:
                current_zero += 1
                while current_zero > k:
                    if nums[start] == 0:
                        current_zero -= 1
                    start += 1
            size_w = end - start + 1
            max_w = max(max_w,size_w)
        return max_w


            
            



            


        