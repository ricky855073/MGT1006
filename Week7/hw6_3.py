#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:13:31 2021

@author: hsienmingliu
"""

string = input()
# string = "Well-known examples include kernel-based approaches, such as Gaussian process regression model (GPR) [1] and support vector regression (SVR) [2], ensemble-based approaches, such as random forest [3], gradient boosting machines [4], and neural-network-based methods [5]."
string_list = string.split()
target_acronym_list = list()

counter = 0

for word in string_list:
    matching_error = 0
    if "(" in word:
        processed_word = word.replace("(", "").replace(")", "")
        length_word = len(processed_word)
        target_word_list = string_list[counter - length_word:counter]
        word_counter = 0
        for j in target_word_list:
            if processed_word[word_counter].lower() != j[0].lower():
                matching_error += 1
                break
            word_counter += 1
        if matching_error == 0:
            fullname = " ".join(target_word_list)
            target_acronym_list.append([processed_word, fullname])
    counter += 1

for i in range(len(target_acronym_list)):
    print(f'{target_acronym_list[i][0]}: {target_acronym_list[i][1]}')


