class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        arr = [[" "] * len(s) for _ in range(n)]
        i = 0
        row = 0
        col = 0
        while(i < len(s)):
            while(row < n and i < len(s)):
                arr[row][col] = s[i]
                row += 1
                i += 1
            row -= 2
            col += 1
            while(row >= 0 and i < len(s)):
                arr[row][col] = s[i]
                col += 1
                row -= 1
                i += 1
            row += 2
        ans = ""
        for i in range(n):
            for j in range(len(s)):
                if arr[i][j] != " ":
                    ans += arr[i][j]
        return ans