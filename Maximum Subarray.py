class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final = nums[0]
        temp = nums[0]
        l = len(nums)
        for i in range(1, l):
            temp = max(nums[i], temp+nums[i])
            final = max(temp, final)	
        return final
