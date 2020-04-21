class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def pro(x):
            x = list(x)
            return "".join(sorted(x))
        name = list(map(pro, strs))
        d = {}
        for i in range(len(name)):
            if name[i] in d.keys():
                d[name[i]].append(strs[i])
            else:
                d[name[i]] = [strs[i]]

        return list(d.values())
