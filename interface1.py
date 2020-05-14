# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:37:40 2020

@author: Siddhant
"""

from tkinter import *
#from config import *

window = Tk()
window.title("Bill Management")
count = 0
item = []
desc = []
rate = []
quantity = []
name = ""
contact = ""
address = ""
error = ""


def itemdetails():
    global count, item, desc, rate, quantity, name, contact, address
    item.append(Entry(window, width = 30, bg = "white"))
    item[count].grid(row = 7+count, column = 0, sticky = W)
    
    desc.append(Entry(window, width = 50, bg = "white"))
    desc[count].grid(row = 7+count, column = 1, sticky = W)
    
    rate.append(Entry(window, width = 30, bg = "white"))
    rate[count].grid(row = 7+count, column = 2, sticky = W)
    
    quantity.append(Entry(window, width = 30, bg = "white"))
    quantity[count].grid(row = 7+count, column = 3, sticky = W)
    count += 1




def inputhandler():
    global item, desc, rate, quantity, name, address, contact, error
    try:
        rate = [float("1") if x == "" else float(x) for x in rate]
        quantity = [float("1") if x == "" else float(x)  for x in quantity]
    except:
        #print("Only numbers accepted for rate and quantity")
        error = "Only numbers accepted for rate and quantity"
    
    
def getter():
    global item, desc, rate, quantity, name, address, contact, error
    item = [x.get() for x in item]
    desc = [x.get() for x in desc]
    rate = [x.get() for x in rate]
    quantity = [x.get() for x in quantity]
    name = name.get()
    address = address.get()
    contact = contact.get()
    inputhandler()
    window.destroy()
    
def layoutgen():
    global name, contact, address, item, desc, rate, quantity, error
    
    Label(window, text = "Enter Customer Details", font = "TimesNewRoman 14 bold") .grid(row = 0, column = 0, columnspan = 10, sticky = W)


    Label(window, text = "Customer Name:", font = "TimesNewRoman 12 bold") .grid(row = 1, column = 0, sticky = W)
    name = Entry(window, width = 70, bg = "white")
    name.grid(row = 1, column = 1, columnspan = 10, sticky = W)

    Label(window, text = "Contact No.:", font = "TimesNewRoman 12 bold") .grid(row = 2, column = 0, sticky = W)
    contact = Entry(window, width = 70, bg = "white")
    contact.grid(row = 2, column = 1, columnspan = 10, sticky = W)

    Label(window, text = "Address:", font = "TimesNewRoman 14 bold") .grid(row = 3, column = 0, sticky = W)
    address = Entry(window, width = 70, bg = "white")
    address.grid(row = 3, column = 1, columnspan = 10, sticky = W)

    Label(window, text = "", font = "TimesNewRoman 14 bold") .grid(row = 4, column = 0, columnspan = 10, sticky = W)

    Label(window, text = "Enter Purchase Details", font = "TimesNewRoman 14 bold") .grid(row = 5, column = 0, columnspan = 10, sticky = W)

    Label(window, text = "Item Name", font = "TimesNewRoman 12 bold")        .grid(row = 6, column = 0, sticky = W)
    Label(window, text = "Item Description", font = "TimesNewRoman 12 bold") .grid(row = 6, column = 1, sticky = W)
    Label(window, text = "Rate", font = "TimesNewRoman 12 bold")             .grid(row = 6, column = 2, sticky = W)
    Label(window, text = "Quantity", font = "TimesNewRoman 12 bold")         .grid(row = 6, column = 3, sticky = W)
    
    itemdetails()

    
    Button(window, text = "SUBMIT", width = 8, command = getter).grid(row = 500, column = 0,sticky = W)
    Button(window, text = "ADD ITEM", width = 8, command = itemdetails).grid(row = 500, column = 1,sticky = W)


layoutgen()
window.mainloop()
