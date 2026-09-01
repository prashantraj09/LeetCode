class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 1 << n
        ans = []
        for i in range(m):
            a = []
            for j in range(n):
                if ((i >> j) % 2 == 1):
                    a.append(nums[j])
            ans.append(a)
        return ans