#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:14:12 2021

@author: hsienmingliu
"""


def mono_inc(inlist, k=3):
    # len_inlist = n, len_diff_list = n - 1
    if k < 3:
        k = 3
    diff_list = list()
    for i in range(len(inlist) - 1):
        diff_list.append(inlist[i + 1] - inlist[i])

    counter = 0
    continue_list = list()
    for i in range(len(diff_list)):
        if diff_list[i] > 0:
            counter += 1
        elif diff_list[i - 1] > 0 and counter >= k:
            continue_list.append([counter, i])
            counter = 0
        else:
            counter = 0
    if counter >= k:
        continue_list.append([counter, len(diff_list)])

    return continue_list


def result_output(result_list):
    if result_list != list():
        print(f'{result_list[0][1] - result_list[0][0]}\n{result_list[0][1]}')
    else:
        print(None)

# RETURN!

def main():
    input_1 = input()
    test_positive = input_1.split(",")
    test_positive = list(map(int, test_positive))
    k = int(input())  # k value
    mono_inc(test_positive, k)
    result_output(mono_inc(test_positive, k))


if __name__ == '__main__':
    main()
