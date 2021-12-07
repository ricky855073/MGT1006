#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:46:42 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()

n = int(input_1)
string = input_2


def preprocess():
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
    return result_list


def counting():
    global word_list, word_dict, filter_dict, sorted_list
    word_list = preprocess()
    word_dict = dict.fromkeys(word_list, 0)

    for word in word_list:
        if word in word_dict:
            count = word_dict[word] + 1
            word_dict.update({word:count})

    filter_dict = dict( (key, value) for (key, value) in word_dict.items() if value >= 2 )
    sorted_list = sorted(filter_dict.items())
    sorted_list = sorted(sorted_list, key=lambda tup: (-tup[1], tup[0]))  # sorts in place

    return sorted_list


def result_output():
    sorted_list = counting()
    if sorted_list != []:
        for row in sorted_list:
            print(row[0], end=" ")
            print(row[1], end="")
            print()
    else:
        print("段落中無重複詞")


def main():
    if n < 2:
        print("ILLEGAL_N")
    else:
        preprocess()
        result_output()


if __name__ == "__main__":
    main()
