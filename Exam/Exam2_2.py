#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:46:31 2021

@author: hsienmingliu
"""

def input_record():
    # input_list可以變動，input_list_copy不動(用來最後輸出用)
    global input_list_copy, input_list
    input_list = list()
    input_list_copy = list()
    string = input()
    while(string != "RECORDSTOP"):
        temp_list = [string.split("_")[0],
                     string.split("_")[1],
                     string.split("_")[2]]
        input_list.append(temp_list)
        string = input()
    input_list_copy = [x[:] for x in input_list]
    return [input_list, input_list_copy]


def discount_remove(input_list):
    index = 0
    index_list = list()

    for row in input_list:
        if float(row[2]) <= 0:
            index_list.append(index)
            index += 1
            continue
        if ('折扣' in row[0]) or ('點數' in row[0]):
            index_list.append(index)
            index += 1
            continue
        if float(row[1]) > 1:
            row[2] = round((float(row[2]) / float(row[1])), 1)

        index += 1

    for i in index_list[::-1]:
        input_list.pop(i)

    return input_list


def result_output():
    global result_list
    result_list = input_list
    result_list = sorted(result_list, key = lambda i: -float(i[2]))

    for row in result_list:
        print(row[0], end=' ')
        print(f'{float(row[2]):.2f}', end='')
        print()


def main():
    input_record()
    discount_remove(input_list)
    result_output()


if __name__ == "__main__":
    main()
