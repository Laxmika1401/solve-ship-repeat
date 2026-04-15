class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        i = 0
        j = 0
        while i<len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merged_nums.append(nums2[j])
                j += 1
            else:
                merged_nums.append(nums1[i])
                i += 1
        
        if i < len(nums1) :
            while(i < len(nums1)):
                merged_nums.append(nums1[i])
                i += 1
        if j < len(nums2) :
            while(j < len(nums2)):
                merged_nums.append(nums2[j])
                j += 1

        k = 0
        l = len(merged_nums)
        if l % 2 >= 1:
            return merged_nums[l//2]

        mid = ((k+l)//2) - 1
        nby2term = merged_nums[mid]
        nby2termplus1 = merged_nums[mid+1] 

        return   (nby2term  + nby2termplus1) / 2

        