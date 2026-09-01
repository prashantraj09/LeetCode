class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            if ((n >> i) % 2 == 1) :
                count += 1
        return count