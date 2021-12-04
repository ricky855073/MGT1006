#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:36:55 2021

@author: hsienmingliu
"""

filepath = input()


process_list = list()
string_list = list()
industry_dict = dict()
dict_keys_list = list()
result_list = list()

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


def median(lst):
    quotient, remainder = divmod(len(lst), 2)
    if remainder:
        return sorted(lst)[quotient]
    return int(round(sum(sorted(lst)[quotient - 1:quotient + 1]) / 2.))


def industry():
    global dict_keys_list, result_list
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
    for item in dict_keys_list:
        counter = 0
        money_list = list()
        for row in process_list[1:]:
            if item == row[8] and industry_dict[item] == row[9]:
                counter += 1
                money_list.append(int(row[4]))
            if item == row[10] and industry_dict[item] == row[11]:
                counter += 1
                money_list.append(int(row[4]))
            if item == row[12] and industry_dict[item] == row[13]:
                counter += 1
                money_list.append(int(row[4]))
            if item == row[14] and industry_dict[item] == row[15]:
                counter += 1
                money_list.append(int(row[4]))
        result_list.append([item, median(money_list), counter])
    result_list = sorted(result_list, key = lambda i : (-i[1], i[0]))


def result_output(result_list):
    for row in result_list[0:10]:
        code = row[0]
        print(f'{code} ', end="")
        print(f'({industry_dict[code]}): ', end="")
        print(f'${row[1]}; ', end="")
        print(f'N={row[2]}', end="")
        print()


def main():
    data_preprocess()
    industry()
    result_output(result_list)


if __name__ == "__main__":
    main()


