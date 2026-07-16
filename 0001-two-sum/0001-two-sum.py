class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in maps:
                return [maps[x], i]
            else:
                maps[nums[i]] = i
        return [0, 0]