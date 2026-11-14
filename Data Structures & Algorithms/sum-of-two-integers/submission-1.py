class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 0000000100
        # 0000000111

        # 0010
        # 0000

        # 1011  if XOR -> 1, if XOR = 0 -> 0 carry 1 bit

        res, carry = 0, 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            res |= (a_bit ^ b_bit ^ carry) << i
            carry = (a_bit & b_bit) | (carry & (a_bit ^ b_bit))
        
        if res >= 1 << 31:        # sign bit set
            res -= 1 << 32        # 4294967291 - 4294967296 = -5
    
        return res

