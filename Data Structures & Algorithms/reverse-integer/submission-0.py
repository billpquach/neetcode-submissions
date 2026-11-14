class Solution:
    def reverse(self, x: int) -> int:
        isNeg = 1
        if x < 0:
            isNeg = -1
            x = abs(x)
        x = str(x)
        x = x[::-1]
        print(x)

        return int(x) * isNeg if abs(int(x)) < 2**31-1 else 0