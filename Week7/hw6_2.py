#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:12:01 2021

@author: hsienmingliu
"""

input_1 = input()
input_2 = input()
input_3 = input()

n = int(input_1)
target_string = input_2
source_string = input_3

# n = 3
# target_string = "今天東北季風增強，水氣增加，雨區擴大到整個北部及東半部地區，整天都有不定時短暫降雨的機會，特別是基隆北海岸雨勢會更明顯，並有局部較大雨勢發生的機率。"
# source_string = "三立氣象專家吳德榮指出，今（21）日鋒面逐漸南下，北台灣及東半部轉為有雨，氣溫漸降，中南部日夜溫差大。明日起至週日鋒面影響及東北季風增強，平地最低溫下探18度，北台灣濕涼，降雨範圍更廣，苗栗以北、東部有較大雨勢。"

def create_continue_str(string, str_list):
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
                str_list.append(string[i:i+n])


def count_similarity(src_str_list, tgt_str_list):
    counter = 0
    target_str_length = len(tgt_str_list)
    match_segment_list = list()
    for i in tgt_str_list:
        for j in src_str_list:
            if i == j:
                counter += 1
                match_segment_list.append(i)
    similarity = counter / target_str_length
    return [target_str_length, counter, similarity, match_segment_list]


def result_output():
    info_list = count_similarity(source_str_list, target_str_list)
    print(f'LEN={info_list[0]}')
    print(f'MATCH_COUNT={info_list[1]}')
    print(f'SIMILARITY={info_list[2]:.4f}')
    print('MATCHED SEGMENTS:')
    for i in info_list[3]:
        print(i)

if n < 2:
    print('ILLEGAL_N')
else:
    punctuation = '。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&\'()*+,-./:;<=>?@[]^_`{¦}~'
    target_str_list = list()
    source_str_list = list()
    create_continue_str(target_string, target_str_list)
    create_continue_str(source_string, source_str_list)
    result_output()
