class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []
        x = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        ans = ""
        for w in s:
            if w in x:
                vowel.append(w)
        j = len(vowel) - 1
        for w in s:
            if w in x:
                ans += vowel[j]
                j -= 1
            else:
                ans += w
        return ans