#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 19:53:14 2021

@author: hsienmingliu
"""

# filepath = input()
filepath = "/Users/hsienmingliu/Desktop/NTU/MGT1006/Week8/test4.csv"


process_list = list()
string_list = list()
industry_dict = dict()
dict_keys_list = list()
result_dict = dict()


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


def counting(first, second, num_list):
    global result_dict, compare_list
    compare_list = f'{num_list[first]} {num_list[second]}'

    if compare_list in result_dict:
        count = result_dict[compare_list] + 1
        result_dict.update({compare_list:count})
    else:
        result_dict.update({compare_list:1})


def industry():
    global dict_keys_list, result_dict
    for row in process_list[1:]:
        industry_dict[row[8]] = row[9]
        industry_dict[row[10]] = row[11]
        industry_dict[row[12]] = row[13]
        industry_dict[row[14]] = row[15]
    try:
        industry_dict.pop('')
    except KeyError:
        pass

    dict_keys_list = list(industry_dict.keys())
    dict_keys_list.sort()

    for row in process_list[1:]:
        num_list = list()
        for i in [row[8], row[10], row[12], row[14]]:
            if i != '':
                num_list.append(i)
            else:
                break
        num_list.sort()
        if len(num_list) < 2:
            continue
        elif len(num_list) == 2:
            counting(0, 1, num_list)
        elif len(num_list) == 3:
            counting(0, 1, num_list)
            counting(0, 2, num_list)
            counting(1, 2, num_list)
        elif len(num_list) == 4:
            counting(0, 1, num_list)
            counting(0, 2, num_list)
            counting(0, 3, num_list)
            counting(1, 2, num_list)
            counting(1, 3, num_list)
            counting(2, 3, num_list)
    result_dict = dict(sorted(result_dict.items(), key=lambda i: (-i[1], i[0])))


def result_output(result_dict):
    global limited_dict
    limited_dict = dict(list(result_dict.items())[0:20])
    for k, v in limited_dict.items():
        index_list = k.split(" ")
        for index in index_list:
            print(industry_dict[index], end=" ")
        print(v, end="")
        print()


def main():
    data_preprocess()
    industry()
    result_output(result_dict)


if __name__ == "__main__":
    main()
