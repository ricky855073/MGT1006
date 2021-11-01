#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:42:51 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()
input_3 = input()

T = int(float(input_1.split(",")[0]) // 1)  # Total time having
N_s = int(input_1.split(",")[1])  # Quantity of people to buy small coal
N_l = int(input_1.split(",")[2])  # Quantity of people to buy large coal
Q_s = int(input_1.split(",")[3])  # Quantity for producing small coal per hour
Q_l = int(input_1.split(",")[4])  # Quantity for producing large coal per hour
R_s = int(input_1.split(",")[5])  # Revenue for small coal
R_l = int(input_1.split(",")[6])  # Revenue for large coal

prob_s_list = list()
prob_l_list = list()
prob_s_cum_list = list()
prob_l_cum_list = list()

revenue_list = list()

# Construct probability list for small coal with total sum
cumulative_prob = 0
for i in range(N_s + 1):
    prob_s_list.append(float(input_2.split(",")[i]))
    cumulative_prob += float(input_2.split(",")[i]) * i
    prob_s_cum_list.append(cumulative_prob)


# Construct probability list for large coal with total sum
cumulative_prob = 0
for j in range(N_l + 1):
    prob_l_list.append(float(input_3.split(",")[j]))
    cumulative_prob += float(input_3.split(",")[j]) * j
    prob_l_cum_list.append(cumulative_prob)


for i in range(T + 1):
    produce_s = i * Q_s
    produce_l = (T - i) * Q_l

    if produce_s > N_s and produce_l > N_l:
        revenue = R_s * prob_s_cum_list[-1] + R_l * prob_l_cum_list[-1]
        revenue_list.append(revenue)

    elif produce_s < N_s and produce_l < N_l:
        revenue = R_s * prob_s_cum_list[produce_s] + R_l * prob_l_cum_list[produce_l]
        revenue_list.append(revenue)

    elif produce_s > N_s and produce_l < N_l:
        revenue = R_s * prob_s_cum_list[-1] + R_l * prob_l_cum_list[produce_l]
        revenue_list.append(revenue)

    elif produce_s < N_s and produce_l > N_l:
        revenue = R_s * prob_s_cum_list[produce_s] + R_l * prob_l_cum_list[-1]
        revenue_list.append(revenue)

print(int(max(revenue_list)))
