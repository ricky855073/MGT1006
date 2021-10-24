#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:23:59 2021

@author: hsienmingliu
"""
input_1 = input()
input_2 = input()
input_3 = input()

# input_1 = "5,10"
# input_2 = "20,90,40,30,100"
# input_3 = "100,30,80,90,20"

n = int(input_1.split(",")[0])
c = int(input_1.split(",")[1])
pq_list = list()
revenue_list = list()


for i in range(n):
    pq_list.append([int(input_2.split(",")[i]), int(input_3.split(",")[i])])
    
# Sorting
pq_list.sort(reverse=True)
    
for i in range(n):
    revenue_list.append([((pq_list[i][0] - c) * pq_list[i][1]), pq_list[i][0]])


print(f'{max(revenue_list)[1]},{max(revenue_list)[0]}')




