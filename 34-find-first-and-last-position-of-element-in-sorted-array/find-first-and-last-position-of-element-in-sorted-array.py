class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = -1
        y = -1
        #for x, first occurence
        low = 0
        high = len(nums) -1
        while (low<= high):
            mid = (low+high)//2
            if nums[mid] == target:
                x = mid
                high = mid - 1 #keep fiinding first
            elif nums[mid] < target:
                low = mid + 1
            else: 
                high = mid - 1
            #should i insert return to exit loop or return at last after both loop are done
        low = 0
        high = len(nums) - 1
        while (low <= high):
            mid = (low+high)//2
            if nums[mid] == target:
                y = mid #store  mid directly as it is an index
                low = mid+1
            elif nums[mid] < target:
                low = mid +1
            else: #mid > target
                high = mid-1
        # return both x and y here
        return [x,y]

        