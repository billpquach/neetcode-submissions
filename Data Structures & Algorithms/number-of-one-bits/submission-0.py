class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # we can shift n's binary >> to & with 1
        # if n & 1, count += 1

        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count