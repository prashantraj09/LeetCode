class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        ans = 0
        while(low <= high):
            h = min(height[low], height[high])
            ans = max(ans, h * (high - low))
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
        return ans