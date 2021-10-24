#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 21:54:28 2021

@author: hsienmingliu
"""

# input_1 = "7,50"
# input_2 = "5,15,4,10,11,16,8"
# input_3 = "6,5,4,4,3,4,1"
# input_4 = "1,1,1,1,0,1,0"

input_1 = input()
input_2 = input()
input_3 = input()
input_4 = input()

n = int(input_1.split(",")[0])
B = int(input_1.split(",")[1])
utility_weight_list = list()
weight_sum = 0
utility_sum = 0

for i in range(n):
    if int(input_4.split(",")[i]) == 1:
        utility_weight_list.append(
            [
                int(input_2.split(",")[i]),
                int(input_3.split(",")[i]),
                int(input_4.split(",")[i]),
            ]
        )
    else:
        continue

for i in range(len(utility_weight_list)):
    utility_sum += utility_weight_list[i][1]
    weight_sum += utility_weight_list[i][0]

if weight_sum <= B:
    print(weight_sum, utility_sum, sep=",")
else:
    print(-1)
