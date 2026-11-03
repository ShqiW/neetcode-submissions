class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.findKth(nums1, nums2, total//2+1)
        if total % 2 == 0:
            left = self.findKth(nums1, nums2, total//2)
            right = self.findKth(nums1, nums2, total//2+1)
            return (left+right)/2
    
    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        if not nums1:
            return nums2[k-1]
        
        if k == 1:
            return min(nums1[0], nums2[0])
        
        idx1 = min(k//2, len(nums1))
        idx2 = k//2

        if nums1[idx1-1] < nums2[idx2-1]:
            return self.findKth(nums1[idx1:], nums2, k-idx1)
        else:
            return self.findKth(nums1, nums2[idx2:], k-idx2)