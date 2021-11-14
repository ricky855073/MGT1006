#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:57:58 2021

@author: hsienmingliu
"""

def input_record():
    # input_list可以變動，input_list_copy不動(用來最後輸出用)
    global input_list, input_list_copy
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


def apply_discount(records):  # record是一個list
    total_discount = float(records[-1][-1])
    total_money = sum(float(records[i][-1]) for i in range(len(records) - 1))

    for i in range(len(records) - 1):
        records[i][-1] = float(records[i][-1]) + (float(records[i][-1]) * total_discount / total_money)
        # discount_list.append(f'{round(price_list[i][-1] * total_discount / total_money, 2):.2f}')
    records.pop(-1)
    return records


def printrec(records):
    for arec in records:
        if abs(arec[2]) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{float(arec[1]):.2f}_{float(arec[2]):.2f}")
    print("---Original---")


def print_original():
    record = input_list_copy
    # print(record)
    for i in range(len(record)):
        print(f'{record[i][0]}_{record[i][1]}_{record[i][2]}')




def main():
    input_record()
    apply_discount(input_list)
    printrec(input_list)  # argument = input_list
    print_original()

if __name__ == "__main__":
    main()


"""
孔雀吉祥捲心禮盒378G_1.00_99.00
肉鋪子-厚感蜜汁豬肉乾 205g_1.00_150.00
華元 波的多洋芋片-蚵仔煎口味315g_2.00_230.00
活動折扣_1.00_-23.00
RECORDSTOP
"""
