#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:36:48 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()
input_3 = input()
input_4 = input()

n = int(input_1.split(",")[0])
B = int(input_1.split(",")[1])
feasible_ans = int(input_4)
utility_weight_list = list()
feasible_set_list = list()
solution_list = list()


for i in range(n):
    utility_weight_list.append([int(input_2.split(",")[i]), int(input_3.split(",")[i])])

for i in range(feasible_ans):
    string = input()
    feasible_set_list.append([int(string.split(",")[0]), string.split(",")[1:]])

for i in range(feasible_ans):
    weight_sum = 0
    utility_sum = 0
    pick_i = int(feasible_set_list[i][0])
    pick = [int(i) for i in (feasible_set_list[i][1])]
    for j in range(len(pick)):
        if pick[j] == 1:
            utility_sum += utility_weight_list[j][1]
            weight_sum += utility_weight_list[j][0]
    solution_list.append([pick_i, weight_sum, utility_sum])

best_solution = solution_list[0][0]
max_weight = solution_list[0][1]
max_utility = solution_list[0][2]

for i in range(len(solution_list)):
    if solution_list[i][1] <= B:
        if solution_list[i][2] > max_utility:
            best_solution = solution_list[i][0]
            max_weight = solution_list[i][1]
            max_utility = solution_list[i][2]
        elif (solution_list[i][2] == max_utility) and (
            solution_list[i][0] < best_solution
        ):
            best_solution = solution_list[i][0]
            max_weight = solution_list[i][1]
            max_utility = solution_list[i][2]
    else:
        continue
print(f"{best_solution},{max_weight},{max_utility}")
