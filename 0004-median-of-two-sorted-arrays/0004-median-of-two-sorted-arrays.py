class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num=sorted(num)
        mid=len(num)//2
        if len(num)%2==0:
            
            return (num[mid]+num[mid-1])/2
        else:
            return num[mid]