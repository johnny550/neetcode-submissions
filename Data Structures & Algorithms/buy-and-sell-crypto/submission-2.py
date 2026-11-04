class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=0,1
        max_profit=0
        while sell<len(prices):
            if prices[sell]>prices[buy]:
                profit=prices[sell]-prices[buy]
                max_profit=max(max_profit,profit)
            else:
                buy=sell
            sell+=1
            print(f"Buy on day {buy} and sell on day {sell} for max profit {max_profit}")
        return max_profit