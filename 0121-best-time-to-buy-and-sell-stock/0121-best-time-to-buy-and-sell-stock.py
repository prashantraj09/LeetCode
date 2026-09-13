class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for a in arr:
            buy = min(buy, a)
            profit = max(profit, a - buy)
        return profit