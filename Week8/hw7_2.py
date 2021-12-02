#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:45:18 2021

@author: hsienmingliu
"""
filepath = input()

string_list = list()
process_list = list()
length_list = list()


def data_preprocess():
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            string_list.append(line.strip())

    for string in string_list:
        process_list.append(string.split(","))

    for i in process_list:
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
        i[0] = i[0].replace('"','')
        i[3] = i[3].replace('"','')


    return process_list

def length_record(process_list):
    for row in process_list:
        temp_list = list()
        for col in row:
            temp_list.append(len(col))
        length_list.append(temp_list)

    for i in range(len(length_list[0])):
        max_len = length_list[0][i]
        for j in range(len(length_list)):
            if length_list[j][i] > max_len:
                max_len = length_list[j][i]
        print(max_len)


def main():
    data_preprocess()
    length_record(process_list)


if __name__ == "__main__":
    main()
