class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = {}
        dic2 = {}
        for s in ransomNote:
            if s in dic1:
                dic1[s] += 1
            else:
                dic1[s] = 1
        for s in magazine:
            if s in dic2:
                dic2[s] += 1
            else:
                dic2[s] = 1
        for key in dic1:
            if key in dic2:
                if dic1[key] <= dic2[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True