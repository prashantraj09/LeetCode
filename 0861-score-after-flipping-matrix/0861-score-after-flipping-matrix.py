class Solution:
    def matrixScore(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])
        for i in range(m):
            if arr[i][0] == 0:
                for j in range(n):
                    arr[i][j] ^= 1
        for j in range(n):
            zeros = 0
            ones = 0
            for i in range(m):
                if arr[i][j] == 0:
                    zeros += 1
                else:
                    ones += 1
            if zeros > ones:
                for i in range(m):
                    arr[i][j] = 1 - arr[i][j]
        sums = 0
        powe = 1
        for j in range(n-1, -1, -1):
            ones = 0
            for i in range(m):
                if arr[i][j] == 1:
                    ones += 1
            sums += (powe * ones)
            powe *= 2
        return sums