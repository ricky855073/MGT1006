n = int(input())

price_star = 0
max_profit = 0
best_i = 0

for i in range(1, n + 1):
    a = int(input())
    b = int(input())
    c = int(input())

    if c > a:
        price = 1000
        profit = 0  # profit
        if max_profit != 0 or price_star != 1000:
            best_i = i
            max_profit = 0
            price_star = 1000
    else:
        for price in range(c + 1, a // b):
            profit = (a - b * price) * (price - c)
            if profit >= max_profit and price > price_star:
                if price > price_star:
                    best_i = i
                    max_profit = profit
                    price_star = price
            else:
                break

print(best_i, int(price_star), int(max_profit), sep=",")
