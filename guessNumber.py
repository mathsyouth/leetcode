class Solution(object):
    def guessNumber(self, n):
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect.bisect(C(), -1, 1, n)
        
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
        
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            lo, hi = ((mid, mid), (mid+1, hi), (lo, mid-1))[guess(mid)]
        return lo
        
    def guessNumber(self, n):
        low, high = 1, n
        mid = (low + high)/2
        while guess(mid) != 0:
            if guess(mid) == 1:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high)/2
        return mid
