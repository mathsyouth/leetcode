class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        s_list = list(s)
        index = []
        letters = []
        for i, letter in enumerate(s_list):
            if letter in vowels:
                index.append(i)
                letters.append(letter)
        start = -1
        for i in index:
            s_list[i] = letters[start]
            start -= 1
        return ''.join(s_list)
