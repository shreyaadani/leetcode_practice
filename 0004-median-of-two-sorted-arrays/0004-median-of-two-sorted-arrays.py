class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        res = [0] * (m + n)          
        p1 = p2 = 0

        for p in range(m + n):
            if p2 >= n or (p1 < m and nums1[p1] <= nums2[p2]):
                res[p] = nums1[p1]
                p1 += 1
            else:
                res[p] = nums2[p2]
                p2 += 1

        total = m + n
        mid = total // 2
        if total % 2 == 0:
            return (res[mid] + res[mid - 1]) / 2   
        else:
            return res[mid]   



        
     