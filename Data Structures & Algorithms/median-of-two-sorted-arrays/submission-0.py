class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2,nums1
        n,m = len(nums1),len(nums2)
        half = (n+m+1)//2
        l,r = 0,n

        while l <=r:
            i = (l+r)//2
            j = half - i

            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < n else float('inf')  
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < m else float('inf')   

            if left1 <= right2 and left2<= right1:
                if (n + m )% 2:
                    return float(max(left1,left2))
                else:
                    return (max(left1,left2) + min(right1,right2)) / 2.0
            elif left1> right2:
                r = i-1
            else:
                l = i+1