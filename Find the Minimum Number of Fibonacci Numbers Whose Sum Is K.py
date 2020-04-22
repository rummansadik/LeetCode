class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def dd(k, count):
            f = [1, 1]
            c = 1
            if k == c:
                count += 1
                return count

            while c <= k:
                c = f[-1] + f[-2]
                if c > k:
                    break
                f.append(c)
            #print(f[-1], k,count)
            if f[-1] == k:
                count += 1
                return count
            else:
                k -= f[-1]
                count += 1
                return dd(k, count)
        return dd(k, 0)
