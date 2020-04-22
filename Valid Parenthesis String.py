class Solution:
    def checkValidString(self, s: str) -> bool:
        a, b = 0, 0
        for i in s:
            if i == "(":
                a += 1
            else:
                a -= 1
            if i != ")":
                b += 1
            else:
                b -= 1

            if b < 0:
                break
            a = max(a, 0)
        return a == 0
