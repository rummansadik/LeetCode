class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        L, R, ans = [0] * l, [0] * l, [0] * l
        L[0] = 1
        for i in range(1, l):
            L[i] = nums[i-1] * L[i-1]
        R[l-1] = 1
        for i in reversed(range(l-1)):
            R[i] = nums[i+1] * R[i+1]

        for i in range(l):
            ans[i] = L[i] * R[i]
        return ans
