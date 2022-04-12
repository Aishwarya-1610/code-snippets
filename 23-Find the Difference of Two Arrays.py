"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff1=[]
        diff2=[]
        for i in range (len(nums1)):
            if nums1[i] not in nums2:
                if nums1[i] not in diff1:
                    diff1.append(nums1[i])
        for j in range (len(nums2)):
            if nums2[j] not in nums1:
                if nums2[j] not in diff2:
                    diff2.append(nums2[j])
        res=[]
        res.append(diff1)
        res.append(diff2)
        return res
