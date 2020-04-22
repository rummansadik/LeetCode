class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        s, c = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            c += dic.get(s - k, 0)
            dic[s] += 1
        return c
