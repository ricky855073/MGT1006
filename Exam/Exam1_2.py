#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:26:27 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()
input_3 = input()

n = int(input_1)
weight_list = list()
summation_list = list()

for i in range(n):
    weight_list.append([int(input_3.split(",")[i]),int(input_2.split(",")[i])])
    summation_list.append(weight_list[i][0] * weight_list[i][1])

total_sum = sum(summation_list)

counter = 0
while total_sum // 10 > 0:
    if total_sum % 10 == 1:
        counter += 1
        total_sum = total_sum // 10
    else:
        total_sum = total_sum // 10
if total_sum == 1:
    counter += 1

print(f'{sum(summation_list)},{counter}')

