class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sDict = [0] * 26
        tDict = [0] * 26

        for i, j in zip(s, t):
            sDict[ord(i)-ord('a')] += 1
            tDict[ord(j)-ord('a')] += 1
        
        return sDict == tDict

        