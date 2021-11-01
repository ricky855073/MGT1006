#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:31:31 2021

@author: hsienmingliu
"""
input_1 = input()
input_2 = input()
input_3 = input()

n = int(input_1.split(",")[0])
threshold = int(input_1.split(",")[1])
drink_price = int(int(input_1.split(",")[2]))  # lower_bound

coin_list = list()  # [price, quantity]
coin_sum = 0

for i in range(n):
    coin_list.append([int(input_2.split(",")[i]), int(input_3.split(",")[i])])
    coin_sum += coin_list[i][0] * coin_list[i][1]

if (coin_sum >= drink_price) and (coin_sum >= threshold):
    coin_sum -= drink_price
else:
    coin_sum

give_mom = coin_sum // 100
remaining = coin_sum % 100

print(f"{remaining},{give_mom * 100}")
