class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        letters = []
        # wasitacaroracatisaw
        for i in s:
            if i.isalpha() or i.isnumeric():
                letters.append(i)

        # initialize two pointers converging
        l, r = 0, len(letters)-1
        while l < r:
            if letters[l] != letters[r]:
                return False
            l += 1
            r -= 1
        return True
