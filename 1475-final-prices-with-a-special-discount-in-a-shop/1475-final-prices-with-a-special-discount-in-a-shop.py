class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ans = []
        for i in range(len(prices)):
            check = True
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    check = False
                    break
            if check:
                ans.append(prices[i])
        return ans