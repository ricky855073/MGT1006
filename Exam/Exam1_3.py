#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:42:40 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()

m = int(input_1.split(",")[0])  # Quantity of goods m
n = int(input_1.split(",")[1])  # Order n
Q = int(input_1.split(",")[2])  # Threshold Q
D = int(input_1.split(",")[3])  # Discount D
price_list= list() # Construct price array
order_total_list = list() # Construct order price array for every individual
order_money_list = list()

# construct price list from input_2
for i in range(m):
    price_list.append(int(input_2.split(",")[i]))

# construct order_price list from input
for i in range(n):
    indiv_order = input() # 準備輸入進來的商品訂單個數
    order_list = list() # 把indiv_order輸入進來的東西創造成為一個list
    order_money = 0 # 總共訂單創造多少錢

    # 先創造order list
    for j in range(m):
        order_list.append(int(indiv_order.split(",")[j]))
        order_money += (order_list[j] * price_list[j])
    order_money_list.append(order_money)

for k in range(m):
    if order_money_list[k] >= Q:
        if order_money_list[k] - D > Q:
            order_total_list.append(order_money_list[k] - D)
        else:
            order_total_list.append(Q)
    else:
        order_total_list.append(order_money_list[k])

print(sum(order_total_list))
