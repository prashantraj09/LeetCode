class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr  = []
        for num in nums1:
            arr.append(num)
        for num in nums2:
            arr.append(num)
        arr.sort()
        if (len(arr) % 2) != 0:
            return arr[len(arr)//2]
        sums = arr[len(arr)//2] + arr[(len(arr)//2) - 1]
        return sums/2