class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n -= (n & -n)
        return n
