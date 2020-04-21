class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def res(s):
            li = ""
            for i in s:
                if i == "#":
                    li = li[:-1]
                else:
                    li += i
            return li
        return res(S) == res(T)
