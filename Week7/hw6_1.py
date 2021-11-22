#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:26:53 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()

n = int(input_1)
string = input_2
if n < 2:
    print("ILLEGAL_N")
else:
    punctuation = '。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&\'()*+,-./:;<=>?@[]^_`{¦}~'
    result_list = list()
    for i in range(len(string)):
        item = string[i:i+n]
        if len(item) == n:
            punct_counter = 0
            for j in item:
                if j in punctuation:
                    punct_counter += 1
                    break
                else:
                    continue
            if punct_counter != 0:
                continue
            else:
                result_list.append(string[i:i+n])

    for item in result_list:
        print(item)
