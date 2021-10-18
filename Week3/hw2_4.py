#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:46:42 2021

@author: hsienmingliu
"""
n = int(input())
t = int(input())
q_1 = int(input())
q_2 = int(input())
time_1 = time_2 = 480 #  everyone has 480 minutes

x_list = list()
p_list = list()
i_list = list()
revenue_list = list()

for i in range(n):
    x_list.append(int(input()))
    p_list.append(int(input())) # Price in total

for i in range(n):
    if (p_list[i] / x_list[i]) < t:
        continue
    else:
        if time_1 < (x_list[i] * q_1) or time_2 < (x_list[i] * q_2):
            continue
        else:   
            time_1 -= x_list[i] * q_1
            time_2 -= x_list[i] * q_2
            revenue_list.append(p_list[i])
            i_list.append(i + 1)



if i_list != list():
    print(','.join(str(e) for e in i_list))
    revenue = sum(revenue_list)
    print(f'{time_1},{time_2},{revenue}')
else:
    print(-1)
    print(f'{time_1},{time_2},0')




