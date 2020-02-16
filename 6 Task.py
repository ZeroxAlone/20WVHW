# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:58:38 2020

@author: lisa_
"""


str1 = input("Enter a string: ")
Count = 0
if str1[:2]!=str1[-2:]:
    print("Invalid format")
else:
    count = 1
    for i in range(len(str1)):
        if str1[i] == "#":
            count += 1
print("The number of surnames: ", count)
        