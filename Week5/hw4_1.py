#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding error on Github, need to fix
# EOL WITH LF

input_1 = input()
input_2 = input()
input_3 = input()
input_4 = input()

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

for i in range(m):
    if coin_sum >= food_list[i]:
        coin_sum -= food_list[i]
        buy_list.append(int(i))
    else:
        continue

print(coin_sum)
