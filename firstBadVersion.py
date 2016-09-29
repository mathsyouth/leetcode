class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        down = 1
        up = n
        while down <= up: 
            cur = (up+down)/2
            if isBadVersion(cur) == False:
                down = cur + 1
            else:
                if cur == 1:
                    return cur
                elif isBadVersion(cur-1) == False:
                    return cur
                else:
                    up = cur - 1
