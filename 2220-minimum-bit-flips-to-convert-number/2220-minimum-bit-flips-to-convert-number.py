class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        y = start ^ goal
        count = 0
        for i in range(31):
            if ((y >> i) % 2 == 1):
                count += 1
        return count