#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:06:06 2021

@author: hsienmingliu
"""
from datetime import datetime

filepath = "/Users/hsienmingliu/Desktop/NTU/MGT1006/Week8/bgm_h1k.csv"
condition = str(9999999)
# filepath = input()
# condition = input()

sp2 = "　"  # 全形空白

process_list = list()
string_list = list()
valid_list = list()

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

    return process_list


def string_matching(condition):
    for i in process_list[1:]:
        target_list = i[1:3]
        for target in target_list:
            if condition in str(target):
                valid_list.append(i)

    if valid_list != []:
        valid_list.sort(key = lambda i: (i[5], -int(i[4]), i[1]))
        return True
    else:
        return False



def output_result(string_list):
    if string_matching(condition) == True:
        for slist in string_list[0:20]:
            date_time = datetime.strptime(str(int(slist[5]) + 19110000), "%Y%m%d").strftime("%Y-%m-%d")
            revenue = f'{int(slist[4]):,}'
            if len(slist[2]) != 0:
                print(slist[3].replace('"','').ljust(20, sp2), end=" ")
                print(f'{slist[1]}({slist[2]})  ', end=" ")
                print(date_time.ljust(20), end=" ")
                print(str(revenue).ljust(20), end=" ")
                print(slist[0].replace('"','').ljust(20))
            else:
                print(slist[3].replace('"','').ljust(20, sp2), end=" ")
                print(slist[1].ljust(20), end=" ")
                print(date_time.ljust(20), end=" ")
                print(str(revenue).ljust(20), end=" ")
                print(slist[0].replace('"','').ljust(20))
    elif string_matching(condition) == False:
        print("NO_DATA_FOUND")




def main():
    data_preprocess()
    output_result(valid_list)


if __name__ == "__main__":
    main()
