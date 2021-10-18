#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:11:46 2021

@author: hsienmingliu
"""
n = int(input()) # threshold
x = int(input()) # 1st payment
y = int(input()) # 2nd payment
r = int(input()) # Total order

if r <= n:
    print(r * x)
else:
    print((r - n) * y + n * x)