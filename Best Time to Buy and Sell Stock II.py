class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 10 ** 4 + 1
        f = -1
        p = 0
        i = 0
        while i < len(prices):
            if prices[i] <= m:
                m = prices[i]
                i += 1
            else:
                while i < len(prices):
                    if prices[i] >= f:
                        f = prices[i]
                        if i == len(prices) - 1:
                            p += f - m
                            return p
                    else:
                        p += f - m
                        m = 10 ** 4 + 1
                        f = -1
                        break
                    i += 1

        return p
