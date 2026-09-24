class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        unique = set()
        ans = []
        sums = 0
        for num in nums:
            if num in unique:
                ans.append(num)
            else:
                unique.add(num)
                sums += num
        total = ((len(nums)) * (len(nums) + 1)) // 2
        ans.append(total - sums)
        return ans