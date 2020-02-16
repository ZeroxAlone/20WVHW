# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:02:26 2020

@author: lisa_
"""


List1 = ['This', 'Is', 'A', 'Camel', 'Case', 'String', '(Empty)', '(Empty)', '(Empty)', '(Empty)']
FinalString = ""
for i in range(10):
    if List1[i]!= '(Empty)':
        String = List1[i]
        FinalString += String
print(FinalString)