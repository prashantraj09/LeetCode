class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for ele in nums:
            xor ^= ele
        mask = (xor & (xor - 1)) ^ xor
        b1 = 0
        b2 = 0
        for ele in nums:
            if (ele & mask) != 0:
                b1 ^= ele
            else:
                b2 ^= ele
        return [b1, b2]