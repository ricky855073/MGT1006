#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_1 = input()
input_2 = input()
input_3 = input()
input_4 = input()

# input_1 = "3,4"
# input_2 = "1,5,10"
# input_3 = "18,6,8"
# input_4 = "50,30,70,10"

n = int(input_1.split(",")[0])
m = int(input_1.split(",")[1])

coin_sum = 0
coin_list = list()
food_list = list()
buy_list = list()


for i in range(n):
    coin_list.append([int(input_2.split(",")[i]), int(input_3.split(",")[i])])
    coin_sum += coin_list[i][0] * coin_list[i][1]

for i in range(m):
    food_list.append(int(input_4.split(",")[i]))

food_list.sort(reverse=True)

for i in range(m):
    if coin_sum >= food_list[i]:
        coin_sum -= food_list[i]
        buy_list.append(int(i))
    else:
        continue

print(f'{coin_sum}')
