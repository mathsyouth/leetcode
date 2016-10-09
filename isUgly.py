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
    
    def isUgly(self, num):
        return num > 0 == 30**32 % num
