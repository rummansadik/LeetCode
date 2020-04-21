class Solution:
    def countElements(self, arr: List[int]) -> int:
        s_arr = sorted(list(set(arr)))
        ans = 0
        for i in range(len(s_arr)-1):
            if s_arr[i + 1] == s_arr[i] + 1:
                ans += arr.count(s_arr[i])
        return ans
