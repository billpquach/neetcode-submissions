class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # we can shift n's binary >> to & with 1
        # if n & 1, count += 1

        # 001100
        # 001011
        # 001000
        # res = 1

        # 001000
        # 000111
        # 000000
        # res = 2
    
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res