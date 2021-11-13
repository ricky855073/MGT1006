#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:57:58 2021

@author: hsienmingliu
"""

def input_record():
    global input_list, input_list_copy
    input_list = list()
    input_list_copy = list()
    string = input()
    while(string != "RECORDSTOP"):
        temp_list = [string.split("_")[0],
                     string.split("_")[1],
                     string.split("_")[2]]
        input_list.append(temp_list)
        input_list_copy = input_list.copy()
        string = input()



def apply_discount(records):
    pass

def printrec(records):
    for arec in records:
        if abs(arec[2]) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{arec[1]:.2f}_{arec[2]:.2f}")


def main():
    input_record()

if __name__ == "__main__":
    main()


"""
孔雀吉祥捲心禮盒378G_1.00_99.00
肉鋪子-厚感蜜汁豬肉乾 205g_1.00_150.00
華元 波的多洋芋片-蚵仔煎口味315g_2.00_230.00
活動折扣_1.00_-23.00
RECORDSTOP
"""
