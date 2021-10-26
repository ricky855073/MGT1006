#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:19:51 2021

@author: hsienmingliu
"""
coin_1 = int(input())
coin_5 = int(input())
coin_10 = int(input())
drink_price = int(input())

coin_sum = (coin_1 * 1) + (coin_5 * 5) + (coin_10 * 10)

if coin_sum >= 100:
    coin_sum -= drink_price
else:
    coin_sum

print(coin_sum)
