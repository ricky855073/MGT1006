#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:16:47 2021

@author: hsienmingliu
"""

input_list = input()
# input_list = "0.272,-0.2996,0.20028,0.5701959999999999,0.47913719999999993,0.5053960399999999,-0.05622277200000003,0.2206440596,-0.10554915828000003,-0.533884410796,-0.09371908755719999,-0.21560336129003999,-0.030922352903027972,0.08835435296788043,-0.2881519529224837,-0.5117063670457386,-0.7381944569320169,-0.9967361198524118,-0.7077152838966883,-0.0354006987276817"
float_list = list(map(float, input_list.split(",")))
G = 2


def variance(float_list, G, mode):
    if mode == 'a':
        temp_list = float_list[: -int(G)]
    elif mode == 'b':
        temp_list = float_list[int(G): ]

    length = len(temp_list)

    mean = sum(temp_list) / length
    denominator = length - 1

    numerator = 0.0
    for i in range(length):
        numerator += (temp_list[i] - mean) ** 2

    var = numerator / denominator

    return var


def covariance(float_list, G):
    list_a = float_list[: -int(G)]
    list_b = float_list[int(G): ]
    length_a = len(list_a)
    length_b = len(list_b)

    mean_a = sum(list_a) / length_a
    mean_b = sum(list_b) / length_b
    denominator = length_a - 1

    numerator = 0.0
    for i in range(len(list_a)):
        numerator += (list_a[i] - mean_a) * (list_b[i] - mean_b)

    cov = numerator / denominator

    return cov


def autocor_2(float_list):
    cov_ab = covariance(float_list, G)
    var_a = variance(float_list, G, 'a')
    var_b = variance(float_list, G, 'b')

    numerator = cov_ab
    denominator = (var_a * var_b) ** 0.5

    cor = numerator / denominator
    if cor < 1e-6:
        result = 0.0000
        print(f'{result:.4f}')
    else:
        result = round(cor, 4)
        print(f'{result:.4f}')




def main():
    autocor_2(float_list)


if __name__ == "__main__":
    main()
