class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        ans = []
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        temp = sorted(dic, key=lambda word: (-dic[word], word))
        return temp[:k]