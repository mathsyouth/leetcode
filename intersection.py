class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
        
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(nums2))
        
import bisect
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == [] or nums2 == []:
            return []
        nums1.sort()
        nums2.sort()
        len1, len2 = len(nums1), len(nums2)
        intersect_nums = []
        if len1 < len2:
            len1, len2 = len2, len1
            nums1, nums2 = nums2, nums1
        start1 = bisect.bisect_left(nums1, nums2[0])
        start2 = 0
        while start1 < len1 and start2 < len2:
            if nums1[start1] > nums2[start2]:
                start2 += 1
            elif nums1[start1] < nums2[start2]:
                start1 += 1
            else:
                if intersect_nums == [] or nums1[start1] > intersect_nums[-1]: 
                    intersect_nums.append(nums1[start1])
                start1 += 1
                start2 += 1
        return intersect_nums
