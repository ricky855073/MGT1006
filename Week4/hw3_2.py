#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:23:59 2021

@author: hsienmingliu
"""
input_1 = input()
input_2 = input()
input_3 = input()


n = int(input_1.split(",")[0])
c = int(input_1.split(",")[1])
pq_list = list()
revenue_list = list()
max_profit_list = list()

for i in range(n):
    pq_list.append([int(input_2.split(",")[i]), int(input_3.split(",")[i])])

pq_list.sort(reverse=True)
for i in range(n):
    revenue_list.append([((pq_list[i][0] - c) * pq_list[i][1]), pq_list[i][0]])
max_profit = max(revenue_list)[0]

for i in range(n):
    if max_profit == revenue_list[i][0]:
        max_profit_list.append(revenue_list[i])

print(f"{max_profit_list[-1][1]},{max_profit_list[-1][0]}")
