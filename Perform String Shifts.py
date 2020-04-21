class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        for i in shift:
            if i[0] == 0:
                s = s[i[1]:] + s[: i[1]]
            else:
                s = s[n - i[1]:] + s[:n - i[1]]
        return s
