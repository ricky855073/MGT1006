#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:14:12 2021

@author: hsienmingliu
"""


def mono_inc(inlist, k=3):
    counter = 0
    start = 0
    end = 0
    modified = 0
    duration = 0
    break_record = 0
    for i in range(len(inlist) - 1):
        if inlist[i + 1] - inlist[i] > 0:
            if modified == 0:
                start = i
                modified = 1
            counter += 1
        else:
            end = i
            counter = 0
            modified = 0
            duration = end - start
            if duration >= k:
                break_record = 1
                break
    if ((inlist[-1] - inlist[-2]) > 0) and end == 0:
        end = len(inlist) - 1
    if (start == 0 and end == 0 and break_record == 1) or end - start < k:
        print(None)
    else:
        print(f'{start}\n{end}')


def main():
    input_1 = input()
    test_positive = input_1.split(",")
    test_positive = list(map(int, test_positive))
    k = int(input())  # k value
    if k < 3:
        k = 3
    # mono_inc(test_positive,k)


if __name__ == '__main__':
    main()
