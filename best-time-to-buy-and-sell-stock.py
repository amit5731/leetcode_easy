def maxProfit(prices) -> int:
        profit=0
        curr=prices[0]
        for num in prices[1:]:
            curr=min(num,curr)
            profit=max(profit,num-curr)
        return profit
