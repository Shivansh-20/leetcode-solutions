class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        all_nums = nums1 + nums2# + [2,4,1,2,1,1]
        #all_nums.sort()
        lent = len(all_nums)
        #return lent//2, lent%2, lent, (lent-1)/2
        if lent%2 == 1:
            return all_nums[int((lent-1)/2)]
        else:
            return (all_nums[int(((lent)/2)-1)] + all_nums[int((lent)/2)])/2
