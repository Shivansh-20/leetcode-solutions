class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while (low<=high):
            mid = (low+high)// 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]: #why equal
                if nums[low] <= target and nums[mid] >= target:
                    high = mid - 1 #
                else:
                    low = mid + 1 #
            else :#nums[high] >= mid:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1