"""

min = 0
max = 0
profit = 0

[7,1,5,3,6,4]

l=0, r=1

itr-1:
    l = 1
    r = 2
itr-2:
    profit = 4
    maxP = max(0,4) = 4
    r = 3
itr-3:
    profit = 2
    maxP = max(4,2) = 4
    r = 4
itr-4:
    profit = 5
    maxP = max(4,5) = 5
    r = 5
itr-5:
    profit = 3
    maxP = max(3,5) = 5
    end of the iteration
"""


def maxProfit(prices):
    l = 0
    r = 1
    maxP = 0
    while r != len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r
        r = r+1
    return maxP

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    max_profit = maxProfit(prices)
    print(max_profit)