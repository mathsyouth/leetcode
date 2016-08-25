from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])
    
    def intersect(self, nums1, nums2):
        a, b = map(Counter, (nums1, nums2))
        return list((a & b).elements())
        

import bisect
class Solution(object):
    def intersect(self, nums1, nums2):
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
                intersect_nums.append(nums1[start1])
                start1 += 1
                start2 += 1
        return intersect_nums
