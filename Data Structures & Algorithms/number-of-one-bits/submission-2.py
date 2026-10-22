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
    
        count = 0
        for i in range(32):
            count += (n >> i) & 1
            
        return count