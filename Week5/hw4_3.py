#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_1 = input()
input_2 = input()

n = int(input_1.split(",")[0])
fire_dept = int(input_1.split(",")[1])  # k
catch_fire = list()  # h
city_matrix = list()  # 2d array constructed by list
fire_dept_building = list()
total_path = 0

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
        each_path_min = 1001  # for default purpose
        fire_dept_candidate = 1  # for default purpose
        if j + 1 not in fire_dept_building:
            for k in range(n):
                if ((k + 1 in fire_dept_building)
                        and (city_matrix[j][k] < each_path_min)):
                    each_path_min = city_matrix[j][k]
                    fire_dept_candidate = j + 1
            each_distance.append([each_path_min, fire_dept_candidate])

    temp_list = list()
    for m in range(len(each_distance)):
        if (max(each_distance)[0]) == (each_distance[m][0]):
            temp_list.append(each_distance[m])
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
print(total_path, end="")
