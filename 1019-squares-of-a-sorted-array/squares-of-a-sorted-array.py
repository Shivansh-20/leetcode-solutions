class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)

        left = 0
        right = len(nums) - 1
        write = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[left] ** 2
                left += 1
            else:
                result[write] = nums[right] ** 2
                right -= 1

            write -= 1

        return result
        '''result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        write = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[write] ** 2
            #move orignal position of right to where ?,asnwered by having an extra pointer
                left += 1
            elif abs(nums[left]) <= abs(nums[right]):
                result[write] = nums[write] ** 2
                right -= 1
            write -= 1
        return result'''




        