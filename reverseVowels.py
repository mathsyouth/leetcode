class Solution(object):
    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
        
    def reverseVowels(self, s):
        vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aAeEiIoOuU'
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while i < j and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i] 
            i += 1
            j -= 1
        return ''.join(L)
