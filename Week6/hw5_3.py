#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:15:09 2021

@author: hsienmingliu
"""

def my_nhi(ylist, htype="Original"):
    if htype != "Original":
        htype = "Normalized"

    sum_y = sum(abs(i) for i in ylist)
    hhi = 0
    n = len(ylist)

    for i in range(len(ylist)):
        s_i = ylist[i] / sum_y
        hhi += s_i ** 2

    if htype == "Original":
        print(f'{hhi:.4f}')
    elif htype == "Normalized":
        hhi_star = (hhi - (1 / n)) / (1 - (1 / n))
        print(f'{hhi_star:.4f}')


def main():
    input_1 = input()
    mode = input()
    revenue_list = input_1.split(",")
    revenue_list = list(map(float, revenue_list))
    my_nhi(revenue_list, mode)


if __name__ == "__main__":
    main()
