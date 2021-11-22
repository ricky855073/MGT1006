#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:18:10 2021

@author: hsienmingliu
"""

# width = int(input())
# input_type = input().split(",")

width = 6
input_type = ['s', 'f', 'f', 's']


def string_process(substring):
    if len(substring) >= width:
        return substring[:width - 1] + "~"
    else:
        return substring


def float_process(substring):
    need_fix = f'{float(substring):.2f}'
    if len(need_fix) >= width:
        return need_fix[:width - 1] + "~"
    else:
        return need_fix


def preprocess():

    condition = 1
    string = input().split(",")
    fixed_list = list()
    while condition == 1:
        counter = 0
        processed_list = list()
        for coltype in input_type:
            if coltype == "s":
                processed_list.append(string_process(string[counter]))
                counter += 1
            elif coltype == "f":
                processed_list.append(float_process(string[counter]))
                counter += 1

        fixed_list.append(processed_list)
        string = input()
        if string == "RECORD_END":
            condition = 0
        else:
            string = string.split(",")
    return fixed_list

def result_output():
    fixed_list = preprocess()
    for i in fixed_list:
        print(i)



def main():
    result_output()


if __name__ == "__main__":
    main()
