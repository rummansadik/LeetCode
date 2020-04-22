class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m+1))
        li = []
        for i in range(len(queries)):
            k = P.index(queries[i])
            li.append(k)
            P = [queries[i]] + P[:k] + P[k+1:] 
        return li
