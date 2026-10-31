class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # initialize two pointers converging
        l, r = 0, len(s)-1
        while l < r:
            # wasitacarofacatisaw?
            print(s[l], s[r])
            while not s[l].isalnum() and l < len(s)-1:
                l += 1
            while not s[r].isalnum() and r > 0:
                r -= 1
            if s[l] != s[r] and l < r:
                return False
            l += 1
            r -= 1

        return True
