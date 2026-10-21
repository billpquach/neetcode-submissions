class Solution:
    def reverseBits(self, n: int) -> int:
        rev_n = 0

        # n: 001001
        # 1: 000001

        # b:     100000
        # rev_n: 000000
        #        100000

        # for _ in range(6):
        #     bit = (n >> i) & 1 
        #     rev_n = rev_n | bit << (5 - i)
        # return rev_n

        for i in range(32):
            bit = (n >> i) & 1 
            rev_n = rev_n | bit << (31 -i)
        return rev_n