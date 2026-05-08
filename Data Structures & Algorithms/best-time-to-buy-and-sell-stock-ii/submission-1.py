class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit

        """
        we will collect all small profit
        f the prices are [a, b, c] and $a < b < c$, 
        you have two choices:Hold: 
        Buy at a and sell at c.
         Profit = $c - a$.Greedy: 
         Buy at a, sell at b, then immediately buy at b and sell at c. 
         Profit = $(b - a) + (c - b)$.
         If you look at the math, $(b - a) + (c - b)$ simplifies to $c - a$. 
        """