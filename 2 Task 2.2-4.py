# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:43:55 2020

@author: lisa_
"""
#2.2
Flag = True
UserID = input("Enter an user ID: ")
for i in range(6):
    Temp = ord(UserID[i])
    if i == 0 and 65<=Temp<=90:
        continue
    if 1<=i<=2 and 97<=Temp<=122:
        continue
    if i >= 3 and 48<=Temp<=57:
        continue 
    else:
        Flag = False
if Flag == True:
    print("Correct Format")
else:
    print("Wrong Format")
    
#2.3
Flag = True
UserID = input("Enter an user ID: ")
for i in range(6):
    Temp = ord(UserID[i])
    if 0<=i<=2 and 65<=Temp<=90 or 97<=Temp<=122:
        continue
    if i >= 3 and 48<=Temp<=57:
        continue 
    else:
        Flag = False
if Flag == True:
    print("Correct Format")
else:
    print("Wrong Format")

#2.4
def ValidateUserID(ThisUserId):
    for i in range(6):
        Temp = ord(ThisUserId[i])
        if i == 0 and 65<=Temp<=90:
            continue
        if 1<=i<=2 and 97<=Temp<=122:
            continue
        if i >= 3 and 48<=Temp<=57:
            continue 
        else:
            Flag = False
    return Flag
        