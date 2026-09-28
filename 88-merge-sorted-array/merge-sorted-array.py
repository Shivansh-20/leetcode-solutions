class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
     p1 = m - 1
     p2 = n - 1
     p3 = m + n - 1 #m+n is size of num1 but m gives last position for p1
     while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else: #nums2[p2] >= nums1[p1]: #if p1 finished but p2 still left (before and)
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1
     return nums1
        

