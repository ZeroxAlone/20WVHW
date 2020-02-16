# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:27:50 2020

@author: lisa_
"""


file = open("BOOK-FILE.txt","r")
IsFound = False 
ThisBook = input("Enter book")
for FileBook in file.readlines():
    if FileBook == ThisBook:
        IsFound = True
        print("BOOK FOUND")
    if IsFound == True:
        break
    else:
        IsFound = False
        print("BOOK NOT FOUND" )
        

