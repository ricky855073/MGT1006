#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ref: https://stackoverflow.com/questions/7845152/deep-copy-nested-list-without-using-the-deepcopy-function
"""
Created on Sat Nov 13 21:57:58 2021

@author: hsienmingliu
"""

def input_record():
    # input_list可以變動，input_list_copy不動(用來最後輸出用)
    global input_list_copy
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


def apply_discount(records):  # record是一個list # error!
    # calculate discount and spending
    total_discount = 0.0
    total_money = 0.0
    for i in range(len(records)):
        if float(records[i][-1]) < 0:
            total_discount += float(records[i][-1])
        else:
            total_money += float(records[i][-1])

    # calculate every item get what amount of discount
    useless_list = list()
    for i in range(len(records)):
        if float(records[i][-1]) >= 0:
            records[i][-1] = float(records[i][-1]) + (float(records[i][-1]) * total_discount / total_money)
        else:
            useless_list.append(i)
    useless_list.sort(reverse=True)
    for i in useless_list:
        del records[i]
    return records


def printrec(records):
    for arec in records:
        if abs(float(arec[2])) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{float(arec[1]):.2f}_{float(arec[2]):.2f}")


# def print_original():
#     record = input_list_copy
#     # print(record)
#     for i in range(len(record)):
#         print(f'{record[i][0]}_{record[i][1]}_{float(record[i][2]):.2f}')


def main():
    printrec(apply_discount(input_record()[0]))  # argument = input_list
    print("---Original---")
    printrec(input_list_copy)

if __name__ == "__main__":
    main()

# ORIGINAL OUTPUT NEED TO BE FLOAT
'''
活動折扣_1.00_-23.00
孔雀吉祥捲心禮盒378G_1.00_99.00
肉鋪子-厚感蜜汁豬肉乾 205g_1.00_150.00
活動折扣_1.00_-23.00
華元 波的多洋芋片-蚵仔煎口味315g_2.00_230.00
活動折扣_1.00_-23.00
RECORDSTOP

'''
