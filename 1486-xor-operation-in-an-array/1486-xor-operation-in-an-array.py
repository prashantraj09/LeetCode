class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = start
        ans = start
        for i in range(1, n):
            nums = (start + (2 * i))
            ans ^= nums
        return ans