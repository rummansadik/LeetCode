class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        while n not in res and n != 1:
            res.append(n)
            n = str(n)
            n = sum(int(i) ** 2 for i in n)
        if n == 1:
            return True
        else:
            return False
