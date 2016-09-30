class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for prime in range(5, 1, -1):
            while num % prime == 0 < num:
                num /= prime
        return num == 1
