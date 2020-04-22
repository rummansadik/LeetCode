class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        li = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and words[j] not in words[i]:
                    li.append(words[i])
                    break
        return li
