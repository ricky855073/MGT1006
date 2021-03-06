#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
# EOF with CRLF

input_1 = input()
input_2 = input()

n = int(input_1)
city_num_list = list()
city_matrix = list() # 2d array constructed by list
best_loc_dist = list()

for i in range(n):
    city_num_list.append(int(input_2.split(",")[i]))

for i in range(n):
    distance = input()
    temp_list = list()
    for j in range(n):
        temp_list.append(int(distance.split(",")[j]))
    city_matrix.append(temp_list)

for i in range(n):
    distance = 0
    for j in range(n):
        distance += city_num_list[j] * city_matrix[j][i]
    best_loc_dist.append([distance, int(i + 1)])

print(f'{min(best_loc_dist)[1]},{min(best_loc_dist)[0]}')
