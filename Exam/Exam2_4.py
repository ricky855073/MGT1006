#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:46:53 2021

@author: hsienmingliu
"""

# filepath = input()
filepath = input()
string_list = list()
length_list = list()
length_set = set()

def read_file(filepath):
    global string_list
    punctuation = '。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&\'()*+,-./:;<=>?@[]^_`{¦}~ \n'
    with open (filepath ,"r", encoding="utf-8") as f:
        for line in f:
            counter = 0
            for char in line:
                if char not in punctuation:
                    counter += 1

            string_list.append([line.strip(), counter])
            length_list.append(counter)

    return string_list


def result_output():
    global process_list, length_list, length_set, big3_list
    process_list = sorted(string_list, key = lambda i: -i[1])
    length_list.sort(reverse=True)
    length_set = set(length_list)
    length_set = sorted(length_set, reverse=True)
    big3_list = length_set[0:3]

    for i in big3_list:
        for row in process_list:
            if row[1] == i:
                print(row[1], end=" ")
                print(row[0], end="")
                print()


def main():
    read_file(filepath)
    result_output()


if __name__ == "__main__":
    main()
