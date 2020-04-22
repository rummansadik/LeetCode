class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        m = []
        for i in range(len(nums)):
            s += nums[i]
            m.append(s)
        x = min(m)
        if x < 0:
            startValue = abs(x) + 1
        else:
            startValue = 1
        return startValue
