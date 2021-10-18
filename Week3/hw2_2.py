#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:22:40 2021

@author: hsienmingliu
"""
n = int(input()) # threshold
m = int(input()) # Aggregate order
x = int(input()) # 1st payment
y = int(input()) # 2nd payment
b = int(input()) # Bonus for over m (This is a constant)
r_1 = int(input()) # Monday order
r_2 = int(input()) # Tuesday order
r_3 = int(input()) # Wednesday order
r_4 = int(input()) # Thursday order
r_5 = int(input()) # Friday order
r_6 = int(input()) # Saturday order
r_7 = int(input()) # Sunday order

weekly_r = [r_1, r_2, r_3, r_4, r_5, r_6, r_7]
bonus = list()

for i in range(7):
    if weekly_r[i] > n:
        bonus.append(weekly_r[i] - n)
    else:
        bonus.append(0)
        
money_sum = 0
weekly_r_sum = 0
for i in range(7):
    weekly_r_sum += weekly_r[i]
    money_sum += bonus[i] * y
    money_sum += (weekly_r[i] - bonus[i]) * x
    

print(money_sum) if weekly_r_sum < m else print(money_sum + b)

    

