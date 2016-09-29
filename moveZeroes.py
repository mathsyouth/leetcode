class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur = 0
        while cur < len(nums) and nums[cur] != 0:
            cur += 1
        zero_pos = cur
        cur += 1
        while cur < len(nums):
            if nums[cur] != 0:
                nums[zero_pos], nums[cur] = nums[cur], nums[zero_pos]
                zero_pos += 1 
            cur += 1                

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        noneZero = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[noneZero] = nums[noneZero], nums[i]
                noneZero += 1
            i += 1
        while noneZero < len(nums):
            nums[noneZero] = 0
            noneZero += 1
