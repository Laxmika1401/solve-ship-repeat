class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = sorted(nums1 + nums2)
        i = 0
        j = len(merged_nums)
        if j % 2 >= 1:
            return merged_nums[j//2]

        mid = ((i+j)//2) - 1
        nby2term = merged_nums[mid]
        nby2termplus1 = merged_nums[mid+1] 

        return   (nby2term  + nby2termplus1) / 2

        