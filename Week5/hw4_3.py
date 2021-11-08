#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_1 = input()
input_2 = input()

n = int(input_1.split(",")[0])
fire_dept = int(input_1.split(",")[1])  # k
catch_fire = list()  # h
city_matrix = list() # 2d array constructed by list
fire_dept_building = list()
total_path = int()

for i in range(n):
    catch_fire.append(int(input_2.split(",")[i]))

# Create Distance Matrix
for i in range(n):
    distance = input()
    temp_list = list()
    for j in range(n):
        temp_list.append(int(distance.split(",")[j]))
    city_matrix.append(temp_list)


# first fire department
first_loc = list()
for i in range(n):
    distance = 0
    for j in range(n):
        distance += catch_fire[j] * city_matrix[j][i]
    first_loc.append([distance, i + 1])
fire_dept_building.append(min(first_loc)[1])

# other fire department
for i in range(fire_dept - 1):
    max_distance = int()
    each_distance = list()
    for j in range(n):
        if j + 1 not in fire_dept_building:
            for k in range(n):
                if k + 1 in fire_dept_building:
                    each_distance.append([city_matrix[j][k], j + 1])
    temp_list = list()
    for l in range(len(each_distance)):
        if (max(each_distance)[0]) == (each_distance[l][0]):
            temp_list.append(each_distance[l])
    fire_dept_building.append(min(temp_list)[1])

# Calculate total path
for i in range(n):
    if i + 1 not in fire_dept_building:
        temp_list = list()
        for j in range(n):
            if j + 1 in fire_dept_building:
                temp_list.append(city_matrix[i][j] * catch_fire[i])
        total_path += min(temp_list)

for i in range(len(fire_dept_building)):
    print(fire_dept_building[i], end="")
    if i != len(fire_dept_building) - 1:
        print(",", end="")
print(";", end="")
print(total_path, end = "")



