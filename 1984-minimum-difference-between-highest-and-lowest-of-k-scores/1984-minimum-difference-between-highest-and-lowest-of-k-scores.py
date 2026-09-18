class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        ans = float ('inf')
        i, j = 0, k - 1
        while (j < len(nums)):
            ans = min(ans, abs(nums[i] - nums[j]))
            i += 1
            j += 1
        return ans