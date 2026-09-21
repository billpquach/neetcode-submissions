class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sLetters = [0] * 26
        tLetters = [0] * 26
        for i, j in zip(s, t):
            sLetters[ord(i)-ord('a')] += 1
            tLetters[ord(j)-ord('a')] += 1
        return sLetters == tLetters
