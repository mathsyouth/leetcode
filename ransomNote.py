class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s1, s2, i = sorted(ransomNote), sorted(magazine), 0
        for c in s2:
            if i==len(s1) or c>s1[i]:
                break
            if c==s1[i]:
                i += 1
        return i==len(s1)
        
    def canConstruct(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
