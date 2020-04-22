class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        li = [1] * len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    li[i] = max(li[j] + 1, li[i])
        return max(li)
