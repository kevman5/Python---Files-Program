# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:26:13 2021

@author: kevmm
"""
AccountInformation = "c:\\users\Public\Documents\\AccountInformation.txt"
f = open(AccountInformation, "w")
f.close()

def CreateRecord():
    AccX = input("Account Type: ")
    AccNum = input("Account Number: ")
    Fname = input("First Name: ")
    Lname = input("Last Name: ")
    TransType = input("Transaction Type: ")
    Amountx = input("Amount your wanting for transaction: ")
    f = open(AccountInformation, "a")
    f.write('%10s,%10s,%10s,%10s,%10s,%10s' % (AccX, AccNum, Fname, Lname, TransType, Amountx))
    f.close()
    print("This record has been created.")


def PrintRecords():
    f = open(AccountInformation, "r")
    for x in f:
        AccX = (x[0:10]).strip()
        AccNum = (x[11:21]).strip()
        Fname = (x[22:32]).strip()
        Lname = (x[33:43]).strip()
        TransType = (x[44:54]).strip()
        Amountx = (x[55:65]).strip()
        print("Account Type: ", AccX)
        print("Account Number: ", AccNum)
        print("First Name: ", Fname)
        print("Last Name: ", Lname)
        print("Transaction Type: ", TransType)
        print("Amount your wanting for transaction: ", Amountx)
        
        
def mainmenu():
            choice = 2
            while choice != 9:
                print("1: Create Record")
                print("2: Print all records")
                print("9: Exit ")
                choice = int(input("Enter # for the menu option you are wanting: "))
                if choice == 1:
                    CreateRecord()
                elif choice == 2:
                    PrintRecords()
mainmenu()