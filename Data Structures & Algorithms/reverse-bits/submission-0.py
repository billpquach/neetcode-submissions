class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # for i in range(6):
        #     bit = (n >> i) & 1
        #     res | (bit << (5-i))
        #   110110
        # bit = 1 ; 
        # res = 000001

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res