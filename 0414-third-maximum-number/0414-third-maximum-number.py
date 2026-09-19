class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = nums[0]
        second = float('-inf')
        third = float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
        if third == float('-inf'):
            return first
        return third