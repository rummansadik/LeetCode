class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li = []
        for i in range(len(nums)):
            if nums[i] == 0:
                li.append(i)

        for i in range(len(li)-1, -1, -1):
            nums.pop(li[i])
        nums += [0] * len(li)
