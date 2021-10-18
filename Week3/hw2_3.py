#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 18:16:23 2021

@author: hsienmingliu
"""
n = int(input())

price_star = 0
max_profit = 0
best_i = 0
no_profit = 0


for i in range(1, n + 1):
    # print(f"This i is {i}")
    a = int(input())
    b = int(input())
    c = int(input())

    if c > a:
        no_profit += 1
        price = 1000
        profit = 0  # profit
        if no_profit == 1:
            if max_profit == 0 and price_star == 0:
                best_i = i
                max_profit = profit
                price_star = price

    else:
        for price in range(a // b, c - 1, -1):
            profit = (a - b * price) * (price - c)
            if profit > max_profit:
                best_i = i
                max_profit = profit
                price_star = price
            elif profit == max_profit:
                max_profit = profit
                price_star = price

print(best_i, int(price_star), int(max_profit), sep=",")
