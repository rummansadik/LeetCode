class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        d = {}
        sub, c = 0, 0
        for i in range(l):
            if nums[i] == 0:
                c -= 1
            else:
                c += 1
            if c == 0:
                sub = i + 1
            if c in d:
                sub = max(sub, i - d[c])
            else:
                d[c] = i
        return sub
