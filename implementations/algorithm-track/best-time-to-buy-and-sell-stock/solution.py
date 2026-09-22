def max_profit_bruteforce(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > best:
                best = profit
    return best


def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for price in prices[1:]:
        profit = price - min_price
        if profit > best:
            best = profit
        if price < min_price:
            min_price = price
    return best
