#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:34:26 2021

@author: hsienmingliu
"""

filepath = input()
process_list_N = int(input())


string_list = list()
with open(filepath, "r", encoding = "utf-8") as f:
    for line in f:
        string_list.append(line.strip())


process_list = list()

for string in string_list:
    process_list.append(string.split(","))

for i in process_list:
    quote_list = list()
    temp_list = list()
    for j in range(len(i)):
        if len(i[j]) == 0:
            continue
        elif i[j][0] == '"' or i[j][-1] == '"':
            if len(i[j].split('"')) != 3:
                temp_list.append(i[j])
    if temp_list != []:
        i[1] = (','.join(temp_list))
    if len(i) != 16:
        i.pop(0)


def output_result(process_list):
    print('營業人名稱:', process_list[3].replace('"',''))
    print('統一編號:', process_list[1])
    print('營業地址:', process_list[0].replace('"',''))

output_result(process_list[process_list_N])







